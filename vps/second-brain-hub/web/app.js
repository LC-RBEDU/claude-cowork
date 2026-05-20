/** One distinct color per slot in proj_order (~13 projects). */
const PROJECT_PALETTE = [
  '#e57373',
  '#64b5f6',
  '#4db6ac',
  '#81c784',
  '#ffb74d',
  '#ba68c8',
  '#f06292',
  '#4dd0e1',
  '#aed581',
  '#ff8a65',
  '#9575cd',
  '#dce775',
  '#90a4ae',
];

function projectColor(slug, index) {
  if (typeof index === 'number' && index >= 0 && index < PROJECT_PALETTE.length) {
    return PROJECT_PALETTE[index];
  }
  let h = 0;
  for (let i = 0; i < slug.length; i++) h = (h * 31 + slug.charCodeAt(i)) | 0;
  return PROJECT_PALETTE[Math.abs(h) % PROJECT_PALETTE.length];
}

/** Mirrors cron/build_dashboard.py project_prefix — fallback when displayId not in JSON. */
function projectPrefix(name) {
  const parts = [];
  for (const word of (name || '').split(/\s+/).slice(0, 3)) {
    const w = word.trim();
    if (w) parts.push(w[0].toUpperCase());
  }
  return parts.join('');
}

function taskIdSuffix(taskId) {
  if (!taskId) return '';
  const suffix = String(taskId).replace(/^[A-Za-z]+/, '');
  return suffix || String(taskId);
}

function taskDisplayId(t, data) {
  if (t.displayId) return t.displayId;
  const slug = t.proj;
  const name = data?.projects?.[slug]?.name || slug;
  const prefix = t.projPrefix || projectPrefix(name);
  const tid = t.id || '';
  return prefix ? prefix + taskIdSuffix(tid) : tid;
}

function resolveTaskColor(t, data) {
  if (t.projColor) return t.projColor;
  const order = data?.proj_order || [];
  const index = order.indexOf(t.proj);
  return projectColor(t.proj, index >= 0 ? index : undefined);
}

function taskProjectStyle(t, data) {
  return {
    displayId: taskDisplayId(t, data),
    projColor: resolveTaskColor(t, data),
  };
}

function applyTaskProjectEl(el, t, data) {
  const { projColor } = taskProjectStyle(t, data);
  if (projColor) {
    el.style.setProperty('--task-proj-color', projColor);
    el.style.borderLeftColor = projColor;
  }
}

async function loadData() {
  if (window.__DASHBOARD_DATA__) return window.__DASHBOARD_DATA__;
  const res = await fetch('dashboard-data.json?' + Date.now());
  if (!res.ok) throw new Error('dashboard-data.json missing — spusť build_dashboard.py');
  return res.json();
}

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s ?? '';
  return d.innerHTML;
}

function iceScore(t) {
  const ice = t?.ice;
  if (!ice) return null;
  const i = ice.i ?? 5;
  const c = ice.c ?? 5;
  const e = Math.max(ice.e ?? 5, 1);
  return (i * c) / e;
}

function iceBadgeHtml(t) {
  const score = iceScore(t);
  if (score == null) return '';
  return `<span class="ice-badge" title="ICE">${score.toFixed(1)}</span>`;
}

function urgencyPillHtml(t) {
  const p = t?.p;
  if (!p) return '';
  const cls = { ASAP: 'asap', Next: 'next', Backlog: 'backlog' }[p] || p.toLowerCase();
  return `<span class="urgency-pill ${cls}">${esc(p)}</span>`;
}

function taskTitleHtml(displayId, t) {
  return `<span class="task-title-meta">
    <strong class="task-id">${esc(displayId)}</strong>
    ${urgencyPillHtml(t)}
    ${iceBadgeHtml(t)}
  </span>
  <span class="task-name">${esc(t.name)}</span>`;
}

function subtaskProgress(ch) {
  if (!ch?.length) return null;
  const done = ch.filter((c) => c.d).length;
  return `${done}/${ch.length}`;
}

function renderSubtasks(ch) {
  if (!ch?.length) return '';
  const items = ch
    .map(
      (c) =>
        `<li class="subtask${c.d ? ' done' : ''}"><span class="chk">${c.d ? '✓' : '○'}</span>${esc(c.t)}</li>`
    )
    .join('');
  return `<ul class="subtasks">${items}</ul>`;
}

/** Task row: expandable when checklist (ch) exists */
function renderTaskRow(t, opts = {}) {
  const progress = subtaskProgress(t.ch);
  const hasCh = Boolean(t.ch?.length);
  const metaHtml = opts.showMeta && t.dl ? `<div class="task-meta">${esc(t.dl)}</div>` : '';
  const displayId = opts.displayId ?? t.displayId ?? t.id;

  if (hasCh) {
    return `<details class="task-details">
      <summary class="task-summary">
        <span class="task-title">${taskTitleHtml(displayId, t)}</span>
        <span class="task-summary-badges"><span class="ch-badge" title="hotovo / celkem">${esc(progress)}</span></span>
      </summary>
      ${renderSubtasks(t.ch)}
      ${metaHtml}
    </details>`;
  }

  return `<div class="task-flat">
    ${taskTitleHtml(displayId, t)}
    ${metaHtml}
  </div>`;
}

function renderTop(data) {
  const el = document.getElementById('top-priority-list');
  el.innerHTML = '';
  (data.topPriority || []).forEach((t) => {
    const div = document.createElement('div');
    div.className = 'card' + (t.p === 'ASAP' ? ' asap' : '');
    const proj = data.projects?.[t.proj]?.name || t.proj;
    const progress = subtaskProgress(t.ch);
    const { displayId } = taskProjectStyle(t, data);
    applyTaskProjectEl(div, t, data);
    const body = renderTaskRow(t, { showMeta: false, displayId });
    div.innerHTML = `${body}
      <div class="proj">${esc(proj)} · ${esc(t.p)}${t.dl ? ' · ' + esc(t.dl) : ''}${
      progress ? ' · checklist ' + esc(progress) : ''
    }</div>`;
    el.appendChild(div);
  });
}

function renderColumns(data) {
  const root = document.getElementById('task-columns');
  const cols = { ASAP: [], Next: [], Backlog: [] };
  (data.tasks || []).forEach((t) => {
    if (t.st === 'dn') return;
    const p = t.p || 'Backlog';
    if (!cols[p]) cols[p] = [];
    cols[p].push(t);
  });
  root.innerHTML = '';
  for (const [key, list] of Object.entries(cols)) {
    const col = document.createElement('details');
    col.className = 'col-details col ' + key.toLowerCase();
    const summary = document.createElement('summary');
    summary.className = 'col-summary';
    summary.textContent = `${key} (${list.length})`;
    col.appendChild(summary);
    const wrap = document.createElement('div');
    wrap.className = 'task-list';
    list.forEach((t) => {
      const item = document.createElement('div');
      item.className = 'task-item';
      const { displayId } = taskProjectStyle(t, data);
      applyTaskProjectEl(item, t, data);
      item.innerHTML = renderTaskRow(t, { showMeta: true, displayId });
      wrap.appendChild(item);
    });
    col.appendChild(wrap);
    root.appendChild(col);
  }
}

function renderByProject(data) {
  const root = document.getElementById('by-project');
  const order = data.proj_order || [];
  root.innerHTML = '';
  order.forEach((slug, index) => {
    const tasks = (data.tasks || []).filter((t) => t.proj === slug && t.st !== 'dn');
    if (!tasks.length) return;
    const name = data.projects?.[slug]?.name || slug;
    const color = projectColor(slug, index);
    const withCh = tasks.filter((t) => t.ch?.length).length;

    const block = document.createElement('details');
    block.className = 'proj-details';
    block.innerHTML = `<summary class="proj-summary" style="--proj-color:${color}">
      <span class="proj-name">${esc(name)}</span>
      <span class="proj-count">${tasks.length} úkolů${withCh ? ` · ${withCh} s checklistem` : ''}</span>
    </summary>`;

    const inner = document.createElement('div');
    inner.className = 'proj-tasks';
    tasks.forEach((t) => {
      const row = document.createElement('div');
      row.className = 'task-item';
      const { displayId } = taskProjectStyle(t, data);
      applyTaskProjectEl(row, t, data);
      row.innerHTML = renderTaskRow(t, { showMeta: true, displayId });
      inner.appendChild(row);
    });
    block.appendChild(inner);
    root.appendChild(block);
  });
}

function formatEventTime(ev) {
  if (ev.allDay) {
    const d = (ev.start || '').slice(0, 10);
    return d ? new Date(d + 'T12:00:00').toLocaleDateString('cs-CZ', { weekday: 'short', day: 'numeric', month: 'numeric' }) + ' (celý den)' : '';
  }
  const start = ev.start ? new Date(ev.start) : null;
  const end = ev.end ? new Date(ev.end) : null;
  if (!start || Number.isNaN(start.getTime())) return '';
  const t0 = start.toLocaleTimeString('cs-CZ', { hour: '2-digit', minute: '2-digit' });
  if (!end || Number.isNaN(end.getTime())) return t0;
  const t1 = end.toLocaleTimeString('cs-CZ', { hour: '2-digit', minute: '2-digit' });
  return `${t0}–${t1}`;
}

function renderCalendar(data) {
  const el = document.getElementById('calendar-root');
  if (!el) return;
  const cal = data.calendar || {};
  const events = cal.events || [];
  if (!events.length) {
    const err = cal.fetchError ? ` (${cal.fetchError})` : '';
    el.innerHTML = `<p class="hint">Kalendář prázdný nebo není nastaven SA${esc(err)}. Viz config.example.env.</p>`;
    return;
  }
  const byDay = {};
  events.forEach((ev) => {
    const key = (ev.start || '').slice(0, 10) || '?';
    if (!byDay[key]) byDay[key] = [];
    byDay[key].push(ev);
  });
  const days = Object.keys(byDay).sort();
  let html = '';
  if (cal.source && cal.source !== 'google_api') {
    html += `<p class="hint cal-meta">Zdroj: ${esc(cal.source)}${cal.fetchError ? ' — ' + esc(cal.fetchError) : ''}</p>`;
  }
  days.forEach((day) => {
    const label = new Date(day + 'T12:00:00').toLocaleDateString('cs-CZ', {
      weekday: 'long',
      day: 'numeric',
      month: 'long',
    });
    html += `<div class="cal-day"><h4 class="cal-day-title">${esc(label)}</h4><ul class="cal-events">`;
    byDay[day].forEach((ev) => {
      const time = formatEventTime(ev);
      const loc = ev.location ? `<span class="cal-loc">${esc(ev.location)}</span>` : '';
      const link = ev.htmlLink
        ? ` <a class="cal-link" href="${esc(ev.htmlLink)}" target="_blank" rel="noopener">↗</a>`
        : '';
      html += `<li class="cal-event"><span class="cal-time">${esc(time)}</span> <span class="cal-title">${esc(ev.title)}</span>${loc}${link}</li>`;
    });
    html += '</ul></div>';
  });
  el.innerHTML = html;
}

function renderInboxBadge(data) {
  const count = data.inboxCount ?? 0;
  const label = `INBOX: ${count}`;
  if (count <= 0) {
    const span = document.createElement('span');
    span.className = 'badge';
    span.id = 'badge-inbox';
    span.textContent = label;
    return span;
  }
  const details = document.createElement('details');
  details.className = 'badge-details';
  details.id = 'badge-inbox';
  const summary = document.createElement('summary');
  summary.className = 'badge';
  summary.textContent = label;
  details.appendChild(summary);
  const list = document.createElement('ul');
  list.className = 'badge-list';
  (data.inboxItems || []).forEach((item) => {
    const li = document.createElement('li');
    const title = item.title || item.filename;
    li.innerHTML = `<span class="badge-item-title">${esc(title)}</span><span class="badge-item-path">${esc(item.path)}</span>`;
    list.appendChild(li);
  });
  details.appendChild(list);
  return details;
}

function renderPendingBadge(data) {
  const count = data.pendingCount ?? 0;
  const label = `Ke schválení: ${count}`;
  if (count <= 0) {
    const span = document.createElement('span');
    span.className = 'badge badge-warn';
    span.id = 'badge-pending';
    span.textContent = label;
    return span;
  }
  const details = document.createElement('details');
  details.className = 'badge-details badge-details-warn';
  details.id = 'badge-pending';
  const summary = document.createElement('summary');
  summary.className = 'badge badge-warn';
  summary.textContent = label;
  details.appendChild(summary);
  const list = document.createElement('ul');
  list.className = 'badge-list';
  (data.pendingItems || []).forEach((item) => {
    const li = document.createElement('li');
    const parts = [item.batchId || item.filename];
    if (item.label) parts.push(item.label);
    else if (item.proposalCount) parts.push(`${item.proposalCount} návrhů`);
    li.innerHTML = `<span class="badge-item-title">${esc(parts.join(' — '))}</span><span class="badge-item-path">${esc(item.filename)}</span>`;
    list.appendChild(li);
  });
  details.appendChild(list);
  return details;
}

function renderBadges(data) {
  const root = document.querySelector('.badges');
  if (!root) return;
  root.replaceChildren(renderInboxBadge(data), renderPendingBadge(data));
}

function renderEdu(data) {
  const el = document.getElementById('edu-news');
  const items = data.eduNews || [];
  if (!items.length) {
    el.innerHTML = '<p class="hint">OPS2 — data z operations projektu (cron edu-news-refresh).</p>';
    return;
  }
  el.innerHTML = '<ul>' + items.map((i) => `<li>${esc(i)}</li>`).join('') + '</ul>';
}

const LIVE_POLL_MS = (() => {
  const sec = parseInt(window.DASHBOARD_POLL_SEC || '10', 10);
  return Number.isFinite(sec) && sec > 0 ? sec * 1000 : 10000;
})();

let lastSeenGenerated = null;

function renderAll(data) {
  const meta = document.getElementById('meta-updated');
  if (meta) {
    meta.textContent = 'Aktualizováno: ' + (data.generated || data.updated || '—');
  }
  renderBadges(data);
  renderTop(data);
  renderCalendar(data);
  renderColumns(data);
  renderByProject(data);
  renderEdu(data);
}

function showFileProtocolHint() {
  const header = document.querySelector('.header');
  if (!header || document.getElementById('live-refresh-hint')) return;
  const p = document.createElement('p');
  p.id = 'live-refresh-hint';
  p.className = 'meta live-refresh-hint';
  p.textContent = 'Auto-refresh: spusť scripts/serve_dashboard.sh';
  header.appendChild(p);
}

function startLiveRefresh(initialData) {
  const proto = location.protocol;
  if (proto === 'file:') {
    showFileProtocolHint();
    return;
  }
  if (proto !== 'http:' && proto !== 'https:') return;

  lastSeenGenerated = initialData?.generated || initialData?.updated || null;

  const poll = async () => {
    try {
      const stampRes = await fetch('./dashboard-build-stamp.json?t=' + Date.now(), {
        cache: 'no-store',
      });
      if (!stampRes.ok) return;
      const stamp = await stampRes.json();
      const gen = stamp.generated;
      if (!gen || gen === lastSeenGenerated) return;
      const dataRes = await fetch('./dashboard-data.json?t=' + Date.now(), { cache: 'no-store' });
      if (!dataRes.ok) return;
      const data = await dataRes.json();
      lastSeenGenerated = data.generated || gen;
      window.__DASHBOARD_DATA__ = data;
      renderAll(data);
    } catch {
      /* ignore transient network errors */
    }
  };

  setInterval(poll, LIVE_POLL_MS);
}

async function main() {
  try {
    const data = await loadData();
    renderAll(data);
    startLiveRefresh(data);
  } catch (e) {
    document.body.insertAdjacentHTML(
      'beforeend',
      `<p class="panel hint">Chyba: ${esc(e.message)}. Spusť build_dashboard.py.</p>`
    );
  }
}

main();
