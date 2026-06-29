const THEME_STORAGE_KEY = "agent-rebel-theme";
const SIDEBAR_STORAGE_KEY = "agent-rebel-sidebar-state";

applyStoredTheme();

document.addEventListener("DOMContentLoaded", () => {
  setupThemeToggle();
  setupSidebarToggle();
  setupMobileMenu();
  setupSidebarStatePersistence();
  applyStoredSidebarState();
  renderIcons();

  const graphEl = document.querySelector("#wiki-graph");
  if (!graphEl || typeof cytoscape === "undefined") return;

  fetch(graphEl.dataset.graphUrl || "/graph.json")
    .then((response) => response.json())
    .then((graph) => renderWikiGraph(graphEl, graph))
    .catch(() => {
      graphEl.innerHTML = '<p class="graph-error">Graph data could not be loaded.</p>';
    });
});

window.addEventListener("pageshow", (event) => {
  if (event.persisted) {
    applyStoredSidebarState();
  }
});

function renderWikiGraph(container, graph) {
  const nodes = new Map();
  const elements = [];

  for (const node of graph.nodes) {
    nodes.set(node.id, true);
    elements.push({
      data: {
        id: node.id,
        label: node.title,
        type: node.type,
        href: `/wiki/${node.id}`,
        weight: node.id === "index" ? 4 : 1,
      },
      classes: `type-${node.type}`,
    });
  }

  for (const edge of graph.edges) {
    if (!nodes.has(edge.target)) {
      nodes.set(edge.target, true);
      elements.push({
        data: {
          id: edge.target,
          label: edge.target,
          type: "missing",
          weight: 1,
        },
        classes: "missing",
      });
    }
    elements.push({
      data: {
        id: `${edge.source}->${edge.target}`,
        source: edge.source,
        target: edge.target,
      },
      classes: edge.broken ? "broken" : "",
    });
  }

  const cy = cytoscape({
    container,
    elements,
    wheelSensitivity: 0.18,
    minZoom: 0.25,
    maxZoom: 2.6,
    style: graphStyle(),
    layout: graphLayout("cose"),
  });
  window.agentRebelGraph = cy;

  cy.on("tap", "node", (event) => {
    const href = event.target.data("href");
    if (href) window.location.href = href;
  });

  cy.on("mouseover", "node", (event) => {
    const node = event.target;
    cy.elements().addClass("dimmed");
    node.closedNeighborhood().removeClass("dimmed").addClass("focused");
  });

  cy.on("mouseout", "node", () => {
    cy.elements().removeClass("dimmed focused");
  });

  document.querySelectorAll("[data-graph-layout]").forEach((button) => {
    button.addEventListener("click", () => {
      cy.layout(graphLayout(button.dataset.graphLayout)).run();
    });
  });

  const fitButton = document.querySelector("[data-graph-fit]");
  if (fitButton) {
    fitButton.addEventListener("click", () => cy.fit(undefined, 48));
  }
}

function applyStoredTheme() {
  let theme = "dark";
  try {
    const storedTheme = localStorage.getItem(THEME_STORAGE_KEY);
    if (storedTheme === "light" || storedTheme === "dark") theme = storedTheme;
  } catch {
    theme = "dark";
  }
  applyTheme(theme);
}

function applyStoredSidebarState() {
  const storedState = readSidebarState();
  const groups = document.querySelectorAll(".nav-group");

  if (!storedState) {
    for (const group of groups) {
      group.open = true;
    }
    syncSidebarToggle();
    return;
  }

  const openGroups = new Set(storedState.openGroups || []);
  for (const group of groups) {
    const key = group.querySelector("summary")?.textContent?.trim() || "";
    group.open = openGroups.has(key);
  }

  syncSidebarToggle();
}

function setupSidebarStatePersistence() {
  const sidebar = document.querySelector(".wiki-nav");
  if (!sidebar) return;

  sidebar.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) return;
    const group = link.closest(".nav-group");
    if (!group) return;
    group.open = false;
    persistSidebarState();
  });

  document.querySelectorAll(".nav-group").forEach((group) => {
    group.addEventListener("toggle", persistSidebarState);
  });
}

function setupSidebarToggle() {
  const button = document.querySelector("[data-sidebar-toggle]");
  if (!button) return;

  button.addEventListener("click", () => {
    setAllSidebarGroupsOpen(!areAllSidebarGroupsOpen());
  });

  syncSidebarToggle();
}

function setAllSidebarGroupsOpen(openAll) {
  const groups = document.querySelectorAll(".nav-group");
  for (const group of groups) {
    group.open = openAll;
  }
  persistSidebarState();
}

function areAllSidebarGroupsOpen() {
  const groups = document.querySelectorAll(".nav-group");
  if (!groups.length) return false;
  return Array.from(groups).every((group) => group.open);
}

function readSidebarState() {
  try {
    const storedState = sessionStorage.getItem(SIDEBAR_STORAGE_KEY);
    if (!storedState) return null;
    return JSON.parse(storedState);
  } catch {
    return null;
  }
}

function persistSidebarState() {
  const openGroups = [];
  document.querySelectorAll(".nav-group").forEach((group) => {
    const summary = group.querySelector("summary")?.textContent?.trim();
    if (group.open && summary) openGroups.push(summary);
  });
  try {
    sessionStorage.setItem(SIDEBAR_STORAGE_KEY, JSON.stringify({ openGroups }));
  } catch {
    // Sidebar state still applies for the current page view when storage is unavailable.
  }

  syncSidebarToggle();
}

function syncSidebarToggle() {
  const button = document.querySelector("[data-sidebar-toggle]");
  if (!button) return;

  const groups = document.querySelectorAll(".nav-group");
  if (!groups.length) {
    button.hidden = true;
    return;
  }

  button.hidden = false;
  const openAll = areAllSidebarGroupsOpen();
  const shouldOpenAll = !openAll;
  const label = shouldOpenAll ? "Open all" : "Close all";
  const icon = button.querySelector("[data-sidebar-icon]");

  button.setAttribute("aria-pressed", String(openAll));
  button.setAttribute("aria-label", label);
  button.setAttribute("title", label);
  if (icon) icon.setAttribute("data-lucide", shouldOpenAll ? "chevrons-down-up" : "chevrons-up-down");
  renderIcons();
}

function setupThemeToggle() {
  const button = document.querySelector("[data-theme-toggle]");
  if (!button) return;

  button.addEventListener("click", () => {
    const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    applyTheme(nextTheme);
    try {
      localStorage.setItem(THEME_STORAGE_KEY, nextTheme);
    } catch {
      // Theme still applies for this page view when storage is unavailable.
    }
    if (window.agentRebelGraph) {
      window.agentRebelGraph.style(graphStyle());
    }
    renderIcons();
  });
  updateThemeToggle(button);
}

function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  const button = document.querySelector("[data-theme-toggle]");
  if (button) updateThemeToggle(button);
}

function updateThemeToggle(button) {
  const isDark = document.documentElement.dataset.theme === "dark";
  const icon = button.querySelector("[data-theme-icon]");
  button.setAttribute("aria-pressed", String(isDark));
  button.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
  button.setAttribute("title", isDark ? "Switch to light theme" : "Switch to dark theme");
  if (icon) icon.setAttribute("data-lucide", isDark ? "moon" : "sun");
}

function setupMobileMenu() {
  const sidebar = document.querySelector(".sidebar");
  const button = document.querySelector("[data-menu-toggle]");
  const menu = document.querySelector("[data-menu]");
  if (!sidebar || !button || !menu) return;

  const setOpen = (isOpen) => {
    sidebar.classList.toggle("is-menu-open", isOpen);
    button.setAttribute("aria-expanded", String(isOpen));
    button.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
    const icon = button.querySelector("[data-menu-icon]");
    if (icon) icon.setAttribute("data-lucide", isOpen ? "x" : "menu");
    renderIcons();
  };

  button.addEventListener("click", () => {
    setOpen(!sidebar.classList.contains("is-menu-open"));
  });

  menu.addEventListener("click", (event) => {
    if (window.matchMedia("(max-width: 760px)").matches && event.target.closest("a")) {
      setOpen(false);
    }
  });
}

function renderIcons() {
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

function graphLayout(name) {
  const layouts = {
    cose: {
      name: "cose",
      animate: true,
      animationDuration: 350,
      fit: true,
      padding: 58,
      nodeRepulsion: 6500,
      idealEdgeLength: 118,
      edgeElasticity: 120,
      nestingFactor: 1.15,
    },
    breadthfirst: {
      name: "breadthfirst",
      directed: true,
      spacingFactor: 1.25,
      animate: true,
      animationDuration: 300,
      fit: true,
      padding: 58,
    },
    concentric: {
      name: "concentric",
      animate: true,
      animationDuration: 300,
      fit: true,
      padding: 58,
      concentric: (node) => node.data("weight") || node.degree(),
      levelWidth: () => 2,
    },
  };
  return layouts[name] || layouts.cose;
}

function graphStyle() {
  const text = cssVar("--text", "#111827");
  const panel = cssVar("--panel", "#ffffff");
  const accent = cssVar("--accent", "#2563eb");
  const accentDark = cssVar("--accent-dark", "#1d4ed8");
  const warn = cssVar("--warn", "#b45309");
  const warnSoft = cssVar("--warn-soft", "#fffbeb");
  const faint = cssVar("--faint", "#94a3b8");

  return [
    {
      selector: "node",
      style: {
        "background-color": panel,
        "border-color": accent,
        "border-width": 2,
        "color": text,
        "font-family": "ui-sans-serif, system-ui, sans-serif",
        "font-size": 12,
        "font-weight": 700,
        "height": "mapData(weight, 1, 4, 34, 52)",
        "label": "data(label)",
        "shape": "round-rectangle",
        "text-background-color": panel,
        "text-background-opacity": 0.86,
        "text-background-padding": 3,
        "text-margin-y": -8,
        "text-max-width": 118,
        "text-wrap": "wrap",
        "text-valign": "top",
        "width": "mapData(weight, 1, 4, 34, 52)",
      },
    },
    {
      selector: ".type-catalog",
      style: {
        "background-color": accent,
        "border-color": accentDark,
        "color": accentDark,
        "height": 58,
        "width": 58,
      },
    },
    {
      selector: ".missing",
      style: {
        "background-color": warnSoft,
        "border-color": warn,
        "border-style": "dashed",
        "color": warn,
      },
    },
    {
      selector: "edge",
      style: {
        "curve-style": "bezier",
        "line-color": faint,
        "opacity": 0.74,
        "target-arrow-color": faint,
        "target-arrow-shape": "triangle",
        "width": 1.6,
      },
    },
    {
      selector: "edge.broken",
      style: {
        "line-color": warn,
        "line-style": "dashed",
        "target-arrow-color": warn,
      },
    },
    {
      selector: ".dimmed",
      style: {
        "opacity": 0.18,
      },
    },
    {
      selector: ".focused",
      style: {
        "opacity": 1,
        "z-index": 10,
      },
    },
  ];
}

function cssVar(name, fallback) {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || fallback;
}
