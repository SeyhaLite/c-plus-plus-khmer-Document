/**
 * Translation UI for the Khmer C++ documentation.
 *
 * Three features, all driven by the build-time file
 * `_static/khmer-index.json` (generated from data/inventory.json):
 *
 *   1. breadcrumbs (Furo does not provide them),
 *   2. a C++ standard selector that hides features newer than the chosen
 *      standard,
 *   3. per-page translation status dots in the sidebar navigation.
 *
 * Everything degrades silently if the index cannot be loaded, so the site
 * remains fully usable without JavaScript.
 */
(function () {
  "use strict";

  var OPTIONS = window.DOCUMENTATION_OPTIONS || {};
  var URL_ROOT = OPTIONS.URL_ROOT || "./";
  var CURRENT_DOC = String(OPTIONS.DOCNAME || "").replace(/^\/+/, "");
  var STORAGE_KEY = "kc-cpp-standard";

  function readStoredStandard() {
    try {
      return window.localStorage.getItem(STORAGE_KEY);
    } catch (error) {
      return null;
    }
  }

  function storeStandard(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, value);
    } catch (error) {
      /* private mode: selection simply does not persist */
    }
  }

  function docNameFromHref(href) {
    if (!href) {
      return "";
    }
    var clean = String(href).split("#")[0].split("?")[0];
    if (/^(?:[a-z]+:)?\/\//i.test(clean) || clean.indexOf("mailto:") === 0) {
      return "";
    }
    if (URL_ROOT !== "./" && clean.indexOf(URL_ROOT) === 0) {
      clean = clean.slice(URL_ROOT.length);
    }
    clean = clean.replace(/^(?:\.\/)+/, "").replace(/\.html$/, "");
    return clean.replace(/\/$/, "");
  }

  function relativeHref(doc) {
    return URL_ROOT + doc + ".html";
  }

  function standardRank(index, name) {
    for (var i = 0; i < index.standards.length; i += 1) {
      if (index.standards[i].id === name) {
        return i;
      }
    }
    return 0;
  }

  function applyStandardFilter(index, selected) {
    var limit = standardRank(index, selected);
    var links = document.querySelectorAll(".sidebar-tree a[data-kc-since]");
    for (var i = 0; i < links.length; i += 1) {
      var link = links[i];
      var rank = standardRank(index, link.getAttribute("data-kc-since"));
      var item = link.closest("li");
      var hide = rank > limit;
      if (item) {
        item.classList.toggle("kc-hidden-by-standard", hide);
      }
    }
  }

  function decorateSidebar(index, selected) {
    var links = document.querySelectorAll(".sidebar-tree a[href]");
    for (var i = 0; i < links.length; i += 1) {
      var link = links[i];
      var doc = docNameFromHref(link.getAttribute("href"));
      var page = index.pages[doc];
      if (!page) {
        continue;
      }
      link.setAttribute("data-kc-doc", doc);
      link.setAttribute("data-kc-since", page.since);
      if (!link.querySelector(".kc-dot")) {
        var dot = document.createElement("span");
        dot.className = "kc-dot kc-dot--" + page.status;
        dot.title = page.status_label;
        dot.setAttribute("aria-hidden", "true");
        link.appendChild(dot);
      }
    }
    if (selected) {
      applyStandardFilter(index, selected);
    }
  }

  function buildStandardSelector(index, selected) {
    var tree = document.querySelector(".sidebar-tree");
    if (!tree || document.querySelector(".kc-std-selector")) {
      return;
    }
    var wrap = document.createElement("div");
    wrap.className = "kc-std-selector";

    var label = document.createElement("label");
    label.setAttribute("for", "kc-standard-select");
    label.textContent = "ស្តង់ដារ C++";

    var select = document.createElement("select");
    select.id = "kc-standard-select";
    for (var i = 0; i < index.standards.length; i += 1) {
      var option = document.createElement("option");
      option.value = index.standards[i].id;
      option.textContent = index.standards[i].label;
      select.appendChild(option);
    }
    select.value = selected;

    var note = document.createElement("p");
    note.className = "kc-std-note";
    note.textContent =
      "លាក់លក្ខណៈដែលថ្មីជាងស្តង់ដារដែលបានជ្រើស។ ជម្រើសរក្សាទុកក្នុងកម្មវិធីរុករក។";

    wrap.appendChild(label);
    wrap.appendChild(select);
    wrap.appendChild(note);
    tree.parentNode.insertBefore(wrap, tree);

    select.addEventListener("change", function () {
      storeStandard(select.value);
      applyStandardFilter(index, select.value);
    });
  }

  function insertBreadcrumbs(index) {
    var article =
      document.querySelector("article[role='main']") ||
      document.querySelector("article") ||
      document.querySelector(".content");
    if (!article || article.querySelector(".kc-breadcrumbs")) {
      return;
    }
    var page = index.pages[CURRENT_DOC];
    var track = page ? index.tracks[page.track] : null;

    var nav = document.createElement("nav");
    nav.className = "kc-breadcrumbs";
    nav.setAttribute("aria-label", "Breadcrumb");

    function add(node) {
      nav.appendChild(node);
    }

    function addSeparator() {
      var sep = document.createElement("span");
      sep.className = "kc-breadcrumbs__sep";
      sep.setAttribute("aria-hidden", "true");
      sep.textContent = "›";
      add(sep);
    }

    var home = document.createElement("a");
    home.href = relativeHref("index");
    home.textContent = "ទំព័រដើម";
    add(home);

    if (track) {
      addSeparator();
      var trackLink = document.createElement("a");
      trackLink.href = relativeHref(track.doc);
      trackLink.textContent = track.title_km;
      add(trackLink);
    }

    if (page) {
      addSeparator();
      var current = document.createElement("span");
      current.setAttribute("aria-current", "page");
      current.textContent = page.title_km;
      add(current);
    }

    article.insertBefore(nav, article.firstChild);
  }

  function init(index) {
    var selected;
    var standards = index.standards || [];
    if (!standards.length) {
      return;
    }
    var last = standards[standards.length - 1].id;
    var stored = readStoredStandard();
    var known = false;
    for (var i = 0; i < standards.length; i += 1) {
      if (standards[i].id === stored) {
        known = true;
      }
    }
    selected = known ? stored : last;

    insertBreadcrumbs(index);
    buildStandardSelector(index, selected);
    decorateSidebar(index, selected);
  }

  function start() {
    if (typeof window.fetch !== "function") {
      return;
    }
    window
      .fetch(URL_ROOT + "_static/khmer-index.json", { cache: "no-cache" })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("index unavailable");
        }
        return response.json();
      })
      .then(init)
      .catch(function () {
        /* Static file:// previews and offline copies simply skip the extra UI. */
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
