document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-sidebar-open]");
  if (!button) return;

  const mode = button.getAttribute("data-sidebar-open");
  const groups = document.querySelectorAll(".nav-group");
  for (const group of groups) {
    group.open = mode === "all";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const graphEl = document.querySelector("#wiki-graph");
  if (!graphEl || typeof cytoscape === "undefined") return;

  fetch(graphEl.dataset.graphUrl || "/graph.json")
    .then((response) => response.json())
    .then((graph) => renderWikiGraph(graphEl, graph))
    .catch(() => {
      graphEl.innerHTML = '<p class="graph-error">Graph data could not be loaded.</p>';
    });
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
  return [
    {
      selector: "node",
      style: {
        "background-color": "#ffffff",
        "border-color": "#2563eb",
        "border-width": 2,
        "color": "#111827",
        "font-family": "ui-sans-serif, system-ui, sans-serif",
        "font-size": 12,
        "font-weight": 700,
        "height": "mapData(weight, 1, 4, 34, 52)",
        "label": "data(label)",
        "shape": "round-rectangle",
        "text-background-color": "#ffffff",
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
        "background-color": "#2563eb",
        "border-color": "#1d4ed8",
        "color": "#1d4ed8",
        "height": 58,
        "width": 58,
      },
    },
    {
      selector: ".missing",
      style: {
        "background-color": "#fffbeb",
        "border-color": "#b45309",
        "border-style": "dashed",
        "color": "#92400e",
      },
    },
    {
      selector: "edge",
      style: {
        "curve-style": "bezier",
        "line-color": "#94a3b8",
        "opacity": 0.74,
        "target-arrow-color": "#94a3b8",
        "target-arrow-shape": "triangle",
        "width": 1.6,
      },
    },
    {
      selector: "edge.broken",
      style: {
        "line-color": "#b45309",
        "line-style": "dashed",
        "target-arrow-color": "#b45309",
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
