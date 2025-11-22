<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Project</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0 solid transparent;
  border-right: 0 solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0 solid transparent;
  border-bottom: 0 solid transparent;
}

/*
 * Lumino
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-CommandPalette-search {
  flex: 0 0 auto;
}

.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-DockPanel {
  z-index: 0;
}

.lm-DockPanel-widget {
  z-index: 0;
}

.lm-DockPanel-tabBar {
  z-index: 1;
}

.lm-DockPanel-handle {
  z-index: 2;
}

.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

.lm-Menu-item {
  display: table-row;
}

.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

.lm-MenuBar-item {
  box-sizing: border-box;
}

.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-SplitPanel-child {
  z-index: 0;
}

.lm-SplitPanel-handle {
  z-index: 1;
}

.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabPanel-tabBar {
  z-index: 1;
}

.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jp-Collapse-header {
  padding: 1px 12px;
  background-color: var(--jp-layout-color1);
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  text-transform: uppercase;
  user-select: none;
}

.jp-Collapser-icon {
  height: 16px;
}

.jp-Collapse-header-collapsed .jp-Collapser-icon {
  transform: rotate(-90deg);
  margin: auto 0;
}

.jp-Collapser-title {
  line-height: 25px;
}

.jp-Collapse-contents {
  padding: 0 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
  --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
  --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
  --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddAboveIcon {
  background-image: var(--jp-icon-add-above);
}

.jp-AddBelowIcon {
  background-image: var(--jp-icon-add-below);
}

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}

.jp-BellIcon {
  background-image: var(--jp-icon-bell);
}

.jp-BugDotIcon {
  background-image: var(--jp-icon-bug-dot);
}

.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}

.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}

.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}

.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}

.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}

.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}

.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}

.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}

.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}

.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}

.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}

.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}

.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}

.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}

.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}

.jp-CodeCheckIcon {
  background-image: var(--jp-icon-code-check);
}

.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}

.jp-CollapseAllIcon {
  background-image: var(--jp-icon-collapse-all);
}

.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}

.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}

.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}

.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}

.jp-DeleteIcon {
  background-image: var(--jp-icon-delete);
}

.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}

.jp-DuplicateIcon {
  background-image: var(--jp-icon-duplicate);
}

.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}

.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}

.jp-ErrorIcon {
  background-image: var(--jp-icon-error);
}

.jp-ExpandAllIcon {
  background-image: var(--jp-icon-expand-all);
}

.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}

.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}

.jp-FileIcon {
  background-image: var(--jp-icon-file);
}

.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}

.jp-FilterDotIcon {
  background-image: var(--jp-icon-filter-dot);
}

.jp-FilterIcon {
  background-image: var(--jp-icon-filter);
}

.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}

.jp-FolderFavoriteIcon {
  background-image: var(--jp-icon-folder-favorite);
}

.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}

.jp-HomeIcon {
  background-image: var(--jp-icon-home);
}

.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}

.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}

.jp-InfoIcon {
  background-image: var(--jp-icon-info);
}

.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}

.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}

.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}

.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}

.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}

.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}

.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}

.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}

.jp-LaunchIcon {
  background-image: var(--jp-icon-launch);
}

.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}

.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}

.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}

.jp-ListIcon {
  background-image: var(--jp-icon-list);
}

.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}

.jp-MoveDownIcon {
  background-image: var(--jp-icon-move-down);
}

.jp-MoveUpIcon {
  background-image: var(--jp-icon-move-up);
}

.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}

.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}

.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}

.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}

.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}

.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}

.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}

.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}

.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}

.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}

.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}

.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}

.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}

.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}

.jp-RunIcon {
  background-image: var(--jp-icon-run);
}

.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}

.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}

.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}

.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}

.jp-ShareIcon {
  background-image: var(--jp-icon-share);
}

.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}

.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}

.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}

.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}

.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}

.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}

.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}

.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}

.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}

.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}

.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}

.jp-UserIcon {
  background-image: var(--jp-icon-user);
}

.jp-UsersIcon {
  background-image: var(--jp-icon-users);
}

.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}

.jp-WordIcon {
  background-image: var(--jp-icon-word);
}

.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-TabBar .lm-TabBar-addButton {
  align-items: center;
  display: flex;
  padding: 4px;
  padding-bottom: 5px;
  margin-right: 1px;
  background-color: var(--jp-layout-color2);
}

.lm-TabBar .lm-TabBar-addButton:hover {
  background-color: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  width: var(--jp-private-horizontal-tab-width);
}

.lm-DockPanel-tabBar .lm-TabBar-content {
  flex: unset;
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}

/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}

.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}

.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}

.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}

.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}

.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}

.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}

.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}

.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}

/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}

.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}

.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}

.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}

.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}

.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}

.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}

/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

.jp-icon-dot[fill] {
  fill: var(--jp-warn-color0);
}

.jp-jupyter-icon-color[fill] {
  fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
}

.jp-notebook-icon-color[fill] {
  fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
}

.jp-json-icon-color[fill] {
  fill: var(--jp-json-icon-color, var(--jp-warn-color1));
}

.jp-console-icon-color[fill] {
  fill: var(--jp-console-icon-color, white);
}

.jp-console-icon-background-color[fill] {
  fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
}

.jp-terminal-icon-color[fill] {
  fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
}

.jp-terminal-icon-background-color[fill] {
  fill: var(
    --jp-terminal-icon-background-color,
    var(--jp-inverse-layout-color2)
  );
}

.jp-text-editor-icon-color[fill] {
  fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
}

.jp-inspector-icon-color[fill] {
  fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* stylelint-disable selector-max-class, selector-max-compound-selectors */

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}

.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* stylelint-enable selector-max-class, selector-max-compound-selectors */

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FormGroup-content fieldset {
  border: none;
  padding: 0;
  min-width: 0;
  width: 100%;
}

/* stylelint-disable selector-max-type */

.jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
  font-size: var(--jp-content-font-size2);
  border-color: var(--jp-input-border-color);
  border-style: solid;
  border-radius: var(--jp-border-radius);
  border-width: 1px;
  padding: 6px 8px;
  background: none;
  color: var(--jp-ui-font-color0);
  height: inherit;
}

.jp-FormGroup-content fieldset input[type='checkbox'] {
  position: relative;
  top: 2px;
  margin-left: 0;
}

.jp-FormGroup-content button.jp-mod-styled {
  cursor: pointer;
}

.jp-FormGroup-content .checkbox label {
  cursor: pointer;
  font-size: var(--jp-content-font-size1);
}

.jp-FormGroup-content .jp-root > fieldset > legend {
  display: none;
}

.jp-FormGroup-content .jp-root > fieldset > p {
  display: none;
}

/** copy of `input.jp-mod-styled:focus` style */
.jp-FormGroup-content fieldset input:focus,
.jp-FormGroup-content fieldset select:focus {
  -moz-outline-radius: unset;
  outline: var(--jp-border-width) solid var(--md-blue-500);
  outline-offset: -1px;
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FormGroup-content fieldset input:hover:not(:focus),
.jp-FormGroup-content fieldset select:hover:not(:focus) {
  background-color: var(--jp-border-color2);
}

/* stylelint-enable selector-max-type */

.jp-FormGroup-content .checkbox .field-description {
  /* Disable default description field for checkbox:
   because other widgets do not have description fields,
   we add descriptions to each widget on the field level.
  */
  display: none;
}

.jp-FormGroup-content #root__description {
  display: none;
}

.jp-FormGroup-content .jp-modifiedIndicator {
  width: 5px;
  background-color: var(--jp-brand-color2);
  margin-top: 0;
  margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
  flex-shrink: 0;
}

.jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
  background-color: var(--jp-error-color0);
  margin-right: 0.5em;
}

/* RJSF ARRAY style */

.jp-arrayFieldWrapper legend {
  font-size: var(--jp-content-font-size2);
  color: var(--jp-ui-font-color0);
  flex-basis: 100%;
  padding: 4px 0;
  font-weight: var(--jp-content-heading-font-weight);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-arrayFieldWrapper .field-description {
  padding: 4px 0;
  white-space: pre-wrap;
}

.jp-arrayFieldWrapper .array-item {
  width: 100%;
  border: 1px solid var(--jp-border-color2);
  border-radius: 4px;
  margin: 4px;
}

.jp-ArrayOperations {
  display: flex;
  margin-left: 8px;
}

.jp-ArrayOperationsButton {
  margin: 2px;
}

.jp-ArrayOperationsButton .jp-icon3[fill] {
  fill: var(--jp-ui-font-color0);
}

button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

/* RJSF form validation error */

.jp-FormGroup-content .validationErrors {
  color: var(--jp-error-color0);
}

/* Hide panel level error as duplicated the field level error */
.jp-FormGroup-content .panel.errors {
  display: none;
}

/* RJSF normal content (settings-editor) */

.jp-FormGroup-contentNormal {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
  margin-left: 7px;
  color: var(--jp-ui-font-color0);
}

.jp-FormGroup-contentNormal .jp-FormGroup-description {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-default {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
  font-size: var(--jp-content-font-size1);
  font-weight: normal;
  min-width: 120px;
}

.jp-FormGroup-contentNormal fieldset:not(:first-child) {
  margin-left: 7px;
}

.jp-FormGroup-contentNormal .field-array-of-string .array-item {
  /* Display `jp-ArrayOperations` buttons side-by-side with content except
    for small screens where flex-wrap will place them one below the other.
  */
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

/* RJSF compact content (metadata-form) */

.jp-FormGroup-content.jp-FormGroup-contentCompact {
  width: 100%;
}

.jp-FormGroup-contentCompact .form-group {
  display: flex;
  padding: 0.5em 0.2em 0.5em 0;
}

.jp-FormGroup-contentCompact
  .jp-FormGroup-compactTitle
  .jp-FormGroup-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
}

.jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
  padding-bottom: 0.3em;
}

.jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
  width: 100%;
  box-sizing: border-box;
}

.jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
  padding-bottom: 7px;
}

.jp-FormGroup-contentCompact
  .jp-objectFieldWrapper
  .jp-objectFieldWrapper
  .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

.jp-FormGroup-contentCompact ul.error-detail {
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  padding-inline-start: 1em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-SidePanel {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  overflow-y: auto;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
}

.jp-SidePanel-header {
  flex: 0 0 auto;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0;
  padding: 2px;
  text-transform: uppercase;
}

.jp-SidePanel-toolbar {
  flex: 0 0 auto;
}

.jp-SidePanel-content {
  flex: 1 1 auto;
}

.jp-SidePanel-toolbar,
.jp-AccordionPanel-toolbar {
  height: var(--jp-private-toolbar-height);
}

.jp-SidePanel-toolbar.jp-Toolbar-micro {
  display: none;
}

.lm-AccordionPanel .jp-AccordionPanel-title {
  box-sizing: border-box;
  line-height: 25px;
  margin: 0;
  display: flex;
  align-items: center;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  font-size: var(--jp-ui-font-size0);
}

.jp-AccordionPanel-title {
  cursor: pointer;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  text-transform: uppercase;
}

.lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
  user-select: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
  transform: rotate(-90deg);
  margin: auto 0;
  height: 16px;
}

.jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
  transform: rotate(0deg);
}

.lm-AccordionPanel .jp-AccordionPanel-toolbar {
  background: none;
  box-shadow: none;
  border: none;
  margin-left: auto;
}

.lm-AccordionPanel .lm-SplitPanel-handle:hover {
  background: var(--jp-layout-color3);
}

.jp-text-truncated {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent::before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent::after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper:not(.multiple) {
  height: 28px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.jp-mod-styled:not([multiple]) {
  height: 32px;
}

select.jp-mod-styled[multiple] {
  max-height: 200px;
  overflow-y: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
  font-family: var(--jp-ui-font-family);
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-switch-color, var(--jp-border-color1));
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 8;
  overflow-x: hidden;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0;
  margin: 0;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0 6px;
  margin: 0;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent > span {
  padding: 0;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-WindowedPanel-outer {
  position: relative;
  overflow-y: auto;
}

.jp-WindowedPanel-inner {
  position: relative;
}

.jp-WindowedPanel-window {
  position: absolute;
  left: 0;
  right: 0;
  overflow: visible;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

body {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

/* Disable native link decoration styles everywhere outside of dialog boxes */
a {
  text-decoration: unset;
  color: unset;
}

a:hover {
  text-decoration: unset;
  color: unset;
}

/* Accessibility for links inside dialog box text */
.jp-Dialog-content a {
  text-decoration: revert;
  color: var(--jp-content-link-color);
}

.jp-Dialog-content a:hover {
  text-decoration: revert;
}

/* Styles for ui-components */
.jp-Button {
  color: var(--jp-ui-font-color2);
  border-radius: var(--jp-border-radius);
  padding: 0 12px;
  font-size: var(--jp-ui-font-size1);

  /* Copy from blueprint 3 */
  display: inline-flex;
  flex-direction: row;
  border: none;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  text-align: left;
  vertical-align: middle;
  min-height: 30px;
  min-width: 30px;
}

.jp-Button:disabled {
  cursor: not-allowed;
}

.jp-Button:empty {
  padding: 0 !important;
}

.jp-Button.jp-mod-small {
  min-height: 24px;
  min-width: 24px;
  font-size: 12px;
  padding: 0 7px;
}

/* Use our own theme for hover styles */
.jp-Button.jp-mod-minimal:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Button.jp-mod-minimal {
  background: none;
}

.jp-InputGroup {
  display: block;
  position: relative;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border: none;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
  padding-bottom: 0;
  padding-top: 0;
  padding-left: 10px;
  padding-right: 28px;
  position: relative;
  width: 100%;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-size: 14px;
  font-weight: 400;
  height: 30px;
  line-height: 30px;
  outline: none;
  vertical-align: middle;
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input:disabled {
  cursor: not-allowed;
  resize: block;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input:disabled ~ span {
  cursor: not-allowed;
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color2);
}

.jp-InputGroupAction {
  position: absolute;
  bottom: 1px;
  right: 0;
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  cursor: not-allowed;
  resize: block;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
  cursor: not-allowed;
}

/* Use our own theme for hover and option styles */
/* stylelint-disable-next-line selector-max-type */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}

select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-StatusBar-Widget {
  display: flex;
  align-items: center;
  background: var(--jp-layout-color2);
  min-height: var(--jp-statusbar-height);
  justify-content: space-between;
  padding: 0 10px;
}

.jp-StatusBar-Left {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-StatusBar-Middle {
  display: flex;
  align-items: center;
}

.jp-StatusBar-Right {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
}

.jp-StatusBar-Item {
  max-height: var(--jp-statusbar-height);
  margin: 0 2px;
  height: var(--jp-statusbar-height);
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--jp-ui-font-color1);
  padding: 0 6px;
}

.jp-mod-highlighted:hover {
  background-color: var(--jp-layout-color3);
}

.jp-mod-clicked {
  background-color: var(--jp-brand-color1);
}

.jp-mod-clicked:hover {
  background-color: var(--jp-brand-color0);
}

.jp-mod-clicked .jp-StatusBar-TextItem {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-StatusBar-HoverItem {
  box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
}

.jp-StatusBar-TextItem {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  line-height: 24px;
  color: var(--jp-ui-font-color1);
}

.jp-StatusBar-GroupItem {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-Statusbar-ProgressCircle svg {
  display: block;
  margin: 0 auto;
  width: 16px;
  height: 24px;
  align-self: normal;
}

.jp-Statusbar-ProgressCircle path {
  fill: var(--jp-inverse-layout-color3);
}

.jp-Statusbar-ProgressBar-progress-bar {
  height: 10px;
  width: 100px;
  border: solid 0.25px var(--jp-brand-color2);
  border-radius: 3px;
  overflow: hidden;
  align-self: center;
}

.jp-Statusbar-ProgressBar-progress-bar > div {
  background-color: var(--jp-brand-color2);
  background-image: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
  background-size: 40px 40px;
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 14px;
  color: #fff;
  text-align: center;
  animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
}

.jp-Statusbar-ProgressBar-progress-bar p {
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: 10px;
  width: 100px;
}

@keyframes jp-Statusbar-ExecutionTime-progress-bar {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 40px 40px;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty::after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px 24px 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-content.jp-Dialog-content-small {
  max-width: 500px;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
  outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
  outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-checkbox {
  padding-right: 5px;
}

.jp-Dialog-checkbox > input:focus-visible {
  outline: 1px solid var(--jp-input-active-border-color);
  outline-offset: 1px;
}

.jp-Dialog-spacer {
  flex: 1 1 auto;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error {
  padding: 6px;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
  width: auto;
  padding: 10px;
  background: var(--jp-error-color3);
  border: var(--jp-border-width) solid var(--jp-error-color1);
  border-radius: var(--jp-border-radius);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  white-space: pre-wrap;
  word-wrap: break-word;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;
  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;
  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #a0f;
  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;
  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;
  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;
  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;
  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;
  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;
  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;
  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;
  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;
  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ff0;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;
  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;
  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;
  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;
  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;
  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;
  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0;
  padding: 0;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}

.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}

.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}

.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}

.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}

.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}

.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}

.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}

.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}

.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}

.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}

.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}

.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}

.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}

.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}

.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}

.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);

  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

/* stylelint-disable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0;
}

/* stylelint-enable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  table-layout: fixed;
  margin-left: auto;
  margin-bottom: 1em;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}

[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}

.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}

.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}

.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}

.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}

.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}

.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}

.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}

.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: var(--jp-ui-font-size0);
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-cursor-backdrop {
  position: fixed;
  width: 200px;
  height: 200px;
  margin-top: -100px;
  margin-left: -100px;
  will-change: transform;
  z-index: 100;
}

.lm-mod-drag-image {
  will-change: transform;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-lineFormSearch {
  padding: 4px 12px;
  background-color: var(--jp-layout-color2);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
  font-size: var(--jp-ui-font-size1);
}

.jp-lineFormCaption {
  font-size: var(--jp-ui-font-size0);
  line-height: var(--jp-ui-font-size1);
  margin-top: 4px;
  color: var(--jp-ui-font-color0);
}

.jp-baseLineForm {
  border: none;
  border-radius: 0;
  position: absolute;
  background-size: 16px;
  background-repeat: no-repeat;
  background-position: center;
  outline: none;
}

.jp-lineFormButtonContainer {
  top: 4px;
  right: 8px;
  height: 24px;
  padding: 0 12px;
  width: 12px;
}

.jp-lineFormButtonIcon {
  top: 0;
  right: 0;
  background-color: var(--jp-brand-color1);
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 4px 6px;
}

.jp-lineFormButton {
  top: 0;
  right: 0;
  background-color: transparent;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
}

.jp-lineFormWrapper {
  overflow: hidden;
  padding: 0 8px;
  border: 1px solid var(--jp-border-color0);
  background-color: var(--jp-input-active-background);
  height: 22px;
}

.jp-lineFormWrapperFocusWithin {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-lineFormInput {
  background: transparent;
  width: 200px;
  height: 100%;
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  line-height: 28px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
  font-family: var(--jp-ui-font-family);
  padding: 2px 1px;
  resize: none;
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  min-width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);

  --jp-private-document-search-button-height: 20px;
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-button-content svg {
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-input-wrapper:focus-within {
  border-color: var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button::before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 35px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-filter-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-filter-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled:hover {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 100%;
  display: grid;
  justify-content: start;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: stretch;
}

.jp-DocumentSearch-search-filter-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-filter {
  display: flex;
  align-items: center;
  user-select: none;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: auto 2px;
  padding: 1px 4px;
  height: calc(var(--jp-private-document-search-button-height) + 2px);
}

.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-ui-font-color1);

  /* height - 2 * (padding of wrapper) */
  line-height: calc(var(--jp-private-document-search-button-height) - 2px);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.cm-editor {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;

  /* Changed to auto to autogrow */
}

.cm-editor pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

.jp-CodeMirrorEditor {
  cursor: text;
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.cm-editor.jp-mod-readOnly .cm-cursor {
  display: none;
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.cm-searching,
.cm-searching span {
  /* `.cm-searching span`: we need to override syntax highlighting */
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.cm-searching::selection,
.cm-searching span::selection {
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.jp-current-match > .cm-searching,
.jp-current-match > .cm-searching span,
.cm-searching > .jp-current-match,
.cm-searching > .jp-current-match span {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.jp-current-match > .cm-searching::selection,
.cm-searching > .jp-current-match::selection,
.jp-current-match > .cm-searching span::selection {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.cm-trailingspace {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
  background-position: center left;
  background-repeat: repeat-x;
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .cm-ySelectionCaret {
  position: relative;
  border-left: 1px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -1px;
  font-size: 0.95em;
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 101;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .cm-ySelectionInfo {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser .jp-SidePanel-content {
  display: flex;
  flex-direction: column;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  flex-wrap: wrap;
  row-gap: 12px;
  border-bottom: none;
  height: auto;
  margin: 8px 12px 0;
  box-shadow: none;
  padding: 0;
  justify-content: flex-start;
}

.jp-FileBrowser-Panel {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0 2px;
  padding: 0 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0;
  padding-right: 2px;
  align-items: center;
  height: unset;
}

.jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
  width: 40px;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileSize-hidden {
  display: none;
}

.jp-FileBrowser .lm-AccordionPanel > h3:first-child {
  display: none;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-headerItem.jp-id-filesize {
  flex: 0 0 75px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-checkboxWrapper {
  /* Increases hit area of checkbox. */
  padding: 4px;
}

.jp-DirListing-header
  .jp-DirListing-checkboxWrapper
  + .jp-DirListing-headerItem {
  padding-left: 4px;
}

.jp-DirListing-content .jp-DirListing-checkboxWrapper {
  position: relative;
  left: -4px;
  margin: -4px 0 -4px -8px;
}

.jp-DirListing-checkboxWrapper.jp-mod-visible {
  visibility: visible;
}

/* For devices that support hovering, hide checkboxes until hovered, selected...
*/
@media (hover: hover) {
  .jp-DirListing-checkboxWrapper {
    visibility: hidden;
  }

  .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
  .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
    visibility: visible;
  }
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemText:focus {
  outline-width: 2px;
  outline-color: var(--jp-inverse-layout-color1);
  outline-style: solid;
  outline-offset: 1px;
}

.jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
  outline-color: var(--jp-layout-color1);
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-itemFileSize {
  flex: 0 0 90px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon::before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-OutputPrompt {
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-prompt {
  display: table-cell;
  vertical-align: top;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea .jp-RenderedText {
  padding-left: 1ch;
}

/**
 * Prompt overlay.
 */

.jp-OutputArea-promptOverlay {
  position: absolute;
  top: 0;
  width: var(--jp-cell-prompt-width);
  height: 100%;
  opacity: 0.5;
}

.jp-OutputArea-promptOverlay:hover {
  background: var(--jp-layout-color2);
  box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
  cursor: zoom-out;
}

.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
  cursor: zoom-in;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

.jp-TrimmedOutputs pre {
  background: var(--jp-layout-color3);
  font-size: calc(var(--jp-code-font-size) * 1.4);
  text-align: center;
  text-transform: uppercase;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/* Hide empty lines in the output area, for instance due to cleared widgets */
.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0;
  width: 100%;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;

  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;

  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0 0.25em;
  margin: 0 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input::placeholder {
  opacity: 0;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

.jp-Stdin-input:focus::placeholder {
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

@media print {
  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-OutputPrompt {
    display: table-row;
    text-align: left;
  }

  .jp-OutputArea-child .jp-OutputArea-output {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }
}

/* Trimmed outputs warning */
.jp-TrimmedOutputs > a {
  margin: 10px;
  text-decoration: none;
  cursor: pointer;
}

.jp-TrimmedOutputs > a:hover {
  text-decoration: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Table of Contents
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toc-active-width: 4px;
}

.jp-TableOfContents {
  display: flex;
  flex-direction: column;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  height: 100%;
}

.jp-TableOfContents-placeholder {
  text-align: center;
}

.jp-TableOfContents-placeholderContent {
  color: var(--jp-content-font-color2);
  padding: 8px;
}

.jp-TableOfContents-placeholderContent > h3 {
  margin-bottom: var(--jp-content-heading-margin-bottom);
}

.jp-TableOfContents .jp-SidePanel-content {
  overflow-y: auto;
}

.jp-TableOfContents-tree {
  margin: 4px;
}

.jp-TableOfContents ol {
  list-style-type: none;
}

/* stylelint-disable-next-line selector-max-type */
.jp-TableOfContents li > ol {
  /* Align left border with triangle icon center */
  padding-left: 11px;
}

.jp-TableOfContents-content {
  /* left margin for the active heading indicator */
  margin: 0 0 0 var(--jp-private-toc-active-width);
  padding: 0;
  background-color: var(--jp-layout-color1);
}

.jp-tocItem {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-tocItem-heading {
  display: flex;
  cursor: pointer;
}

.jp-tocItem-heading:hover {
  background-color: var(--jp-layout-color2);
}

.jp-tocItem-content {
  display: block;
  padding: 4px 0;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.jp-tocItem-collapser {
  height: 20px;
  margin: 2px 2px 0;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}

.jp-tocItem-collapser:hover {
  background-color: var(--jp-layout-color3);
}

/* Active heading indicator */

.jp-tocItem-heading::before {
  content: ' ';
  background: transparent;
  width: var(--jp-private-toc-active-width);
  height: 24px;
  position: absolute;
  left: 0;
  border-radius: var(--jp-border-radius);
}

.jp-tocItem-heading.jp-tocItem-active::before {
  background-color: var(--jp-brand-color1);
}

.jp-tocItem-heading:hover.jp-tocItem-active::before {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;

  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Hiding collapsers in print mode.

Note: input and output wrappers have "display: block" propery in print mode.
*/

@media print {
  .jp-Collapser {
    display: none;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-InputArea-editor {
  display: table-cell;
  overflow: hidden;
  vertical-align: top;

  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  display: table-cell;
  vertical-align: top;
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-InputArea-editor {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }

  .jp-InputPrompt {
    display: table-row;
    text-align: left;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: table;
  table-layout: fixed;
  width: 100%;
}

.jp-Placeholder-prompt {
  display: table-cell;
  box-sizing: border-box;
}

.jp-Placeholder-content {
  display: table-cell;
  padding: 4px 6px;
  border: 1px solid transparent;
  border-radius: 0;
  background: none;
  box-sizing: border-box;
  cursor: pointer;
}

.jp-Placeholder-contentContainer {
  display: flex;
}

.jp-Placeholder-content:hover,
.jp-InputPlaceholder > .jp-Placeholder-content:hover {
  border-color: var(--jp-layout-color3);
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

.jp-PlaceholderText {
  white-space: nowrap;
  overflow-x: hidden;
  color: var(--jp-inverse-layout-color3);
  font-family: var(--jp-code-font-family);
}

.jp-InputPlaceholder > .jp-Placeholder-content {
  border-color: var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0;
  margin: 0;

  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 24em;
  margin-left: var(--jp-private-cell-scrolling-output-offset);
  resize: vertical;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
  max-height: unset;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
  content: ' ';
  box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
  width: 100%;
  height: 100%;
  position: sticky;
  bottom: 0;
  top: 0;
  margin-top: -50%;
  float: left;
  display: block;
  pointer-events: none;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
  padding-top: 6px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
  left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  display: table-cell;
  width: 100%;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
.jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  font-size: var(--jp-code-font-size);
  position: absolute;
  background-color: transparent;
  background-size: 25px;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: top;
  background-image: var(--jp-icon-caret-down);
  right: 0;
  top: 0;
  bottom: 0;
}

.jp-collapseHeadingButton.jp-mod-collapsed {
  background-image: var(--jp-icon-caret-right);
}

/*
 set the container font size to match that of content
 so that the nested collapse buttons have the right size
*/
.jp-MarkdownCell .jp-InputPrompt {
  font-size: var(--jp-content-font-size1);
}

/*
  Align collapseHeadingButton with cell top header
  The font sizes are identical to the ones in packages/rendermime/style/base.css
*/
.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
  font-size: var(--jp-content-font-size5);
  background-position-y: calc(0.3 * var(--jp-content-font-size5));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
  font-size: var(--jp-content-font-size4);
  background-position-y: calc(0.3 * var(--jp-content-font-size4));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
  font-size: var(--jp-content-font-size3);
  background-position-y: calc(0.3 * var(--jp-content-font-size3));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
  font-size: var(--jp-content-font-size2);
  background-position-y: calc(0.3 * var(--jp-content-font-size2));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
  font-size: var(--jp-content-font-size1);
  background-position-y: top;
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
  font-size: var(--jp-content-font-size0);
  background-position-y: top;
}

/* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
  display: none;
}

.jp-Notebook.jp-mod-showHiddenCellsButton
  :is(.jp-MarkdownCell:hover, .jp-mod-active)
  .jp-collapseHeadingButton {
  display: flex;
}

/* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
  display: flex;
}

.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-showHiddenCellsButton {
  display: none;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Using block instead of flex to allow the use of the break-inside CSS property for
cell outputs.
*/

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
}

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: var(--jp-notebook-toolbar-padding);

  /* disable paint containment from lumino 2.0 default strict CSS containment */
  contain: style size !important;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

.jp-Toolbar-responsive-popup {
  position: absolute;
  height: fit-content;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: var(--jp-notebook-toolbar-padding);
  z-index: 1;
  right: 0;
  top: 0;
}

.jp-Toolbar > .jp-Toolbar-responsive-opener {
  margin-left: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-Notebook-ExecutionIndicator {
  position: relative;
  display: inline-block;
  height: 100%;
  z-index: 9997;
}

.jp-Notebook-ExecutionIndicator-tooltip {
  visibility: hidden;
  height: auto;
  width: max-content;
  width: -moz-max-content;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color1);
  text-align: justify;
  border-radius: 6px;
  padding: 0 5px;
  position: fixed;
  display: table;
}

.jp-Notebook-ExecutionIndicator-tooltip.up {
  transform: translateX(-50%) translateY(-100%) translateY(-32px);
}

.jp-Notebook-ExecutionIndicator-tooltip.down {
  transform: translateX(calc(-100% + 16px)) translateY(5px);
}

.jp-Notebook-ExecutionIndicator-tooltip.hidden {
  display: none;
}

.jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
  visibility: visible;
}

.jp-Notebook-ExecutionIndicator span {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  color: var(--jp-ui-font-color1);
  line-height: 24px;
  display: block;
}

.jp-Notebook-ExecutionIndicator-progress-bar {
  display: flex;
  justify-content: center;
  height: 100%;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * Execution indicator
 */
.jp-tocItem-content::after {
  content: '';

  /* Must be identical to form a circle */
  width: 12px;
  height: 12px;
  background: none;
  border: none;
  position: absolute;
  right: 0;
}

.jp-tocItem-content[data-running='0']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background: none;
}

.jp-tocItem-content[data-running='1']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background-color: var(--jp-inverse-layout-color3);
}

.jp-tocItem-content[data-running='0'],
.jp-tocItem-content[data-running='1'] {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Notebook-footer {
  height: 27px;
  margin-left: calc(
    var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
      var(--jp-cell-padding)
  );
  width: calc(
    100% -
      (
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
          var(--jp-cell-padding) + var(--jp-cell-padding)
      )
  );
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  color: var(--jp-ui-font-color3);
  margin-top: 6px;
  background: none;
  cursor: pointer;
}

.jp-Notebook-footer:focus {
  border-color: var(--jp-cell-editor-active-border-color);
}

/* For devices that support hovering, hide footer until hover */
@media (hover: hover) {
  .jp-Notebook-footer {
    opacity: 0;
  }

  .jp-Notebook-footer:focus,
  .jp-Notebook-footer:hover {
    opacity: 1;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-side-by-side-output-size: 1fr;
  --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

/* stylelint-disable selector-max-class */

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}

.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-ActiveCellTool {
  padding: 12px 0;
  display: flex;
}

.jp-ActiveCellTool-Content {
  flex: 1 1 auto;
}

.jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
  background: var(--jp-cell-editor-background);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  min-height: 29px;
}

.jp-ActiveCellTool .jp-InputPrompt {
  min-width: calc(var(--jp-cell-prompt-width) * 0.75);
}

.jp-ActiveCellTool-CellContent > pre {
  padding: 5px 4px;
  margin: 0;
  white-space: normal;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label,
.jp-NumberSetter label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0;
}

.jp-NumberSetter input {
  width: 100%;
  margin-top: 4px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Side-by-side Mode (.jp-mod-sideBySide)
|----------------------------------------------------------------------------*/
.jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
  margin-top: 3em;
  margin-bottom: 3em;
  margin-left: 5%;
  margin-right: 5%;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-output-size)
    );
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'header header header'
    'input handle output'
    'footer footer footer';
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-resized-cell)
    );
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
  grid-area: header;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
  grid-area: input;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
  /* overwrite the default margin (no vertical separation needed in side by side move */
  margin-top: 0;
  grid-area: output;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
  grid-area: footer;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
  grid-area: handle;
  user-select: none;
  display: block;
  height: 100%;
  cursor: ew-resize;
  padding: 0 var(--jp-cell-padding);
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
  content: '';
  display: block;
  background: var(--jp-border-color2);
  height: 100%;
  width: 5px;
}

.jp-mod-sideBySide.jp-Notebook
  .jp-CodeCell.jp-mod-resizedCell
  .jp-CellResizeHandle::after {
  background: var(--jp-border-color0);
}

.jp-CellResizeHandle {
  display: none;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
    0 1px 1px 0 var(--jp-shadow-penumbra-color),
    0 1px 3px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
    0 2px 2px 0 var(--jp-shadow-penumbra-color),
    0 1px 5px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
    0 4px 5px 0 var(--jp-shadow-penumbra-color),
    0 1px 10px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
    0 6px 10px 0 var(--jp-shadow-penumbra-color),
    0 1px 18px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
    0 8px 10px 1px var(--jp-shadow-penumbra-color),
    0 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
    0 12px 17px 2px var(--jp-shadow-penumbra-color),
    0 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
    0 16px 24px 2px var(--jp-shadow-penumbra-color),
    0 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
    0 20px 31px 3px var(--jp-shadow-penumbra-color),
    0 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
    0 24px 38px 3px var(--jp-shadow-penumbra-color),
    0 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-inverse-border-color: var(--md-grey-600);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;
  --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
    helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;
  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);
  --jp-content-link-color: var(--md-blue-900);
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);
  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);
  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);
  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);
  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;
  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);
  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;

  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-inverse-border-color);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #a2f;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #a2f;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /*
    RTC user specific colors.
    These colors are used for the cursor, username in the editor,
    and the icon of the user.
  */

  --jp-collaborator-color1: #ffad8e;
  --jp-collaborator-color2: #dac83d;
  --jp-collaborator-color3: #72dd76;
  --jp-collaborator-color4: #00e4d0;
  --jp-collaborator-color5: #45d4ff;
  --jp-collaborator-color6: #e2b1ff;
  --jp-collaborator-color7: #ff9de6;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);

  /* Button colors */
  --jp-accept-color-normal: var(--md-blue-700);
  --jp-accept-color-hover: var(--md-blue-800);
  --jp-accept-color-active: var(--md-blue-900);
  --jp-warn-color-normal: var(--md-red-700);
  --jp-warn-color-hover: var(--md-red-800);
  --jp-warn-color-active: var(--md-red-900);
  --jp-reject-color-normal: var(--md-grey-600);
  --jp-reject-color-hover: var(--md-grey-700);
  --jp-reject-color-active: var(--md-grey-800);

  /* File or activity icons and switch semantic variables */
  --jp-jupyter-icon-color: #f37626;
  --jp-notebook-icon-color: #f37626;
  --jp-json-icon-color: var(--md-orange-700);
  --jp-console-icon-background-color: var(--md-blue-700);
  --jp-console-icon-color: white;
  --jp-terminal-icon-background-color: var(--md-grey-800);
  --jp-terminal-icon-color: var(--md-grey-200);
  --jp-text-editor-icon-color: var(--md-grey-700);
  --jp-inspector-icon-color: var(--md-grey-700);
  --jp-switch-color: var(--md-grey-400);
  --jp-switch-true-position-color: var(--md-orange-900);
}
</style>
<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.cm-editor.cm-s-jupyter .highlight pre {
/* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
  padding: var(--jp-code-padding) 4px;
  margin: 0;

  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  color: inherit;

}

.jp-OutputArea-output pre {
  line-height: inherit;
  font-family: inherit;
}

.jp-RenderedText pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@page {
    margin: 0.5in; /* Margin for each printed piece of paper */
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}
</style>
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                messageStyle: 'none',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
<!-- End of mathjax configuration --><script type="module">
  document.addEventListener("DOMContentLoaded", async () => {
    const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
    // do not load mermaidjs if not needed
    if (!diagrams.length) {
      return;
    }
    const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.7.0/mermaid.esm.min.mjs")).default;
    const parser = new DOMParser();

    mermaid.initialize({
      maxTextSize: 100000,
      maxEdges: 100000,
      startOnLoad: false,
      fontFamily: window
        .getComputedStyle(document.body)
        .getPropertyValue("--jp-ui-font-family"),
      theme: document.querySelector("body[data-jp-theme-light='true']")
        ? "default"
        : "dark",
    });

    let _nextMermaidId = 0;

    function makeMermaidImage(svg) {
      const img = document.createElement("img");
      const doc = parser.parseFromString(svg, "image/svg+xml");
      const svgEl = doc.querySelector("svg");
      const { maxWidth } = svgEl?.style || {};
      const firstTitle = doc.querySelector("title");
      const firstDesc = doc.querySelector("desc");

      img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
      if (maxWidth) {
        img.width = parseInt(maxWidth);
      }
      if (firstTitle) {
        img.setAttribute("alt", firstTitle.textContent);
      }
      if (firstDesc) {
        const caption = document.createElement("figcaption");
        caption.className = "sr-only";
        caption.textContent = firstDesc.textContent;
        return [img, caption];
      }
      return [img];
    }

    async function makeMermaidError(text) {
      let errorMessage = "";
      try {
        await mermaid.parse(text);
      } catch (err) {
        errorMessage = `${err}`;
      }

      const result = document.createElement("details");
      result.className = 'jp-RenderedMermaid-Details';
      const summary = document.createElement("summary");
      summary.className = 'jp-RenderedMermaid-Summary';
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.innerText = text;
      pre.appendChild(code);
      summary.appendChild(pre);
      result.appendChild(summary);

      const warning = document.createElement("pre");
      warning.innerText = errorMessage;
      result.appendChild(warning);
      return [result];
    }

    async function renderOneMarmaid(src) {
      const id = `jp-mermaid-${_nextMermaidId++}`;
      const parent = src.parentNode;
      let raw = src.textContent.trim();
      const el = document.createElement("div");
      el.style.visibility = "hidden";
      document.body.appendChild(el);
      let results = null;
      let output = null;
      try {
        let { svg } = await mermaid.render(id, raw, el);
        svg = cleanMermaidSvg(svg);
        results = makeMermaidImage(svg);
        output = document.createElement("figure");
        results.map(output.appendChild, output);
      } catch (err) {
        parent.classList.add("jp-mod-warning");
        results = await makeMermaidError(raw);
        output = results[0];
      } finally {
        el.remove();
      }
      parent.classList.add("jp-RenderedMermaid");
      parent.appendChild(output);
    }


    /**
     * Post-process to ensure mermaid diagrams contain only valid SVG and XHTML.
     */
    function cleanMermaidSvg(svg) {
      return svg.replace(RE_VOID_ELEMENT, replaceVoidElement);
    }


    /**
     * A regular expression for all void elements, which may include attributes and
     * a slash.
     *
     * @see https://developer.mozilla.org/en-US/docs/Glossary/Void_element
     *
     * Of these, only `<br>` is generated by Mermaid in place of `\n`,
     * but _any_ "malformed" tag will break the SVG rendering entirely.
     */
    const RE_VOID_ELEMENT =
      /<\s*(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\s*([^>]*?)\s*>/gi;

    /**
     * Ensure a void element is closed with a slash, preserving any attributes.
     */
    function replaceVoidElement(match, tag, rest) {
      rest = rest.trim();
      if (!rest.endsWith('/')) {
        rest = `${rest} /`;
      }
      return `<${tag} ${rest}>`;
    }

    void Promise.all([...diagrams].map(renderOneMarmaid));
  });
</script>
<style>
  .jp-Mermaid:not(.jp-RenderedMermaid) {
    display: none;
  }

  .jp-RenderedMermaid {
    overflow: auto;
    display: flex;
  }

  .jp-RenderedMermaid.jp-mod-warning {
    width: auto;
    padding: 0.5em;
    margin-top: 0.5em;
    border: var(--jp-border-width) solid var(--jp-warn-color2);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .jp-RenderedMermaid figure {
    margin: 0;
    overflow: auto;
    max-width: 100%;
  }

  .jp-RenderedMermaid img {
    max-width: 100%;
  }

  .jp-RenderedMermaid-Details > pre {
    margin-top: 1em;
  }

  .jp-RenderedMermaid-Summary {
    color: var(--jp-warn-color2);
  }

  .jp-RenderedMermaid:not(.jp-mod-warning) pre {
    display: none;
  }

  .jp-RenderedMermaid-Summary > pre {
    display: inline-block;
    white-space: normal;
  }
</style>
<!-- End of mermaid configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=32ba59ca-8329-4232-9d80-5ef872986010">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># מטרת הפרויקט- להסיק מסקנות ותובנות לגבי אופי ואופן התרומות שהתקבלו בעמותה בשנים האחרונות על מנת לתכנן ולייעל את תהליכי גיוס התרומות בעתיד</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=f0916c50-9b21-45b1-bf64-9a2a0e82b11b">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># השאלות המחקריות והמסקנות רשומות לאורך הפרויקט, לפני ואחרי כל ניתוח</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=de355128-b5ab-4825-891b-7a33c00d83bf">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># על מנת לבצע את הניתוח יש להשתמש בספריות הבאות:</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=23c8f1f4-a983-4e13-9e57-52afd2a9343a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">pd</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">seaborn</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">sb</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">matplotlib</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">ml</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">matplotlib.pyplot</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">plt</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pyodbc</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">sqlalchemy</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=9f639f46-3515-44c3-ad37-56c4d68b7915">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># ייבוא של בסיס הנתונים מSQL</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=c4b305ef-3dae-42d6-9d17-c1870266e5b6">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">conn_str</span> <span class="o">=</span> <span class="p">(</span>
    <span class="s2">"Driver={SQL Server};"</span>
    <span class="s2">"Server=MC-AOIUL4UH\SQLEXPRESS;"</span>  
    <span class="s2">"Database=Donations;"</span>
    <span class="s2">"Trusted_Connection=yes;"</span>
<span class="p">)</span>

<span class="c1"># יצירת החיבור</span>
<span class="n">conn</span> <span class="o">=</span> <span class="n">pyodbc</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">conn_str</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=970c5bb3-4a75-4581-ac19-8a565f4dae55">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [3]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">regions</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="s2">"SELECT * FROM Regions"</span><span class="p">,</span> <span class="n">conn</span><span class="p">)</span>
<span class="n">donors</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="s2">"SELECT * FROM Donors"</span><span class="p">,</span> <span class="n">conn</span><span class="p">)</span>
<span class="n">donations</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="s2">"SELECT * FROM Donations"</span><span class="p">,</span> <span class="n">conn</span><span class="p">)</span>
<span class="n">credit</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="s2">"SELECT * FROM CreditDetails"</span><span class="p">,</span> <span class="n">conn</span><span class="p">)</span>
<span class="n">checks</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="s2">"SELECT * FROM CheckDetails"</span><span class="p">,</span> <span class="n">conn</span><span class="p">)</span>
<span class="n">receipts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="s2">"SELECT * FROM Receipts"</span><span class="p">,</span> <span class="n">conn</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>C:\Users\User\AppData\Local\Temp\ipykernel_7864\1908869311.py:1: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  regions = pd.read_sql("SELECT * FROM Regions", conn)
C:\Users\User\AppData\Local\Temp\ipykernel_7864\1908869311.py:2: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  donors = pd.read_sql("SELECT * FROM Donors", conn)
C:\Users\User\AppData\Local\Temp\ipykernel_7864\1908869311.py:3: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  donations = pd.read_sql("SELECT * FROM Donations", conn)
C:\Users\User\AppData\Local\Temp\ipykernel_7864\1908869311.py:4: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  credit = pd.read_sql("SELECT * FROM CreditDetails", conn)
C:\Users\User\AppData\Local\Temp\ipykernel_7864\1908869311.py:5: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  checks = pd.read_sql("SELECT * FROM CheckDetails", conn)
C:\Users\User\AppData\Local\Temp\ipykernel_7864\1908869311.py:6: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  receipts = pd.read_sql("SELECT * FROM Receipts", conn)
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=382ed460-bef3-4b5c-a7ed-8bdfd1855d97">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># לאחר ייבוא הנתונים ממסד הנתונים שבנוי ב-SQL Server, מתקבלים מספר DataFrames בפייתון,</span>
<span class="c1"># כאשר כל אחד מהם מייצג טבלה מתוך בסיס הנתונים של מערכת ניהול התורמים והתרומות של העמותה.</span>

<span class="c1"># 1. טבלת Regions (אזורים)</span>
<span class="c1"># טבלה זו מתארת את חלוקת הארץ לאזורים שונים שבהם מתגוררים התורמים.</span>
<span class="c1"># לכל אזור יש מזהה ייחודי (RegionID), שם אזור (RegionName) ושם מנהל האזור (Manager).</span>
<span class="c1"># הטבלה מאפשרת ניתוח של נתוני התרומות לפי אזור גאוגרפי או לפי מנהל אחראי.</span>

<span class="c1"># 2. טבלת Donors (תורמים)</span>
<span class="c1"># טבלה זו מכילה את פרטיהם האישיים של התורמים: שם פרטי, שם משפחה, תעודת זהות, כתובת, עיר, טלפון וכתובת דוא"ל.</span>
<span class="c1"># בנוסף, לכל תורם מצוין האזור שאליו הוא משתייך באמצעות עמודת RegionID, שהיא מפתח זר לטבלת האזורים.</span>
<span class="c1"># באמצעות טבלה זו ניתן לקשר בין התרומות לתורמים ולנתח את תרומת האוכלוסייה לפי אזור מגורים, עיר או פרטים דמוגרפיים אחרים.</span>

<span class="c1"># 3. טבלת Donations (תרומות)</span>
<span class="c1"># זוהי הטבלה המרכזית שמתארת את כל התרומות שהתקבלו בעמותה.</span>
<span class="c1"># העמודות כוללות את מזהה התרומה (DonationID), מזהה התורם (DonorID),</span>
<span class="c1"># סוג התרומה (Type – לדוגמה: אשראי, צ’ק, מזומן, העברה בנקאית), תאריך התרומה (Date) וסכום התרומה (Amount).</span>
<span class="c1"># טבלה זו מאפשרת לבצע ניתוחים כספיים – כמו סכום התרומות הכולל, ממוצעים, והשוואות בין סוגי תרומות שונים או בין תקופות שונות.</span>

<span class="c1"># 4. טבלת CreditDetails (פרטי אשראי)</span>
<span class="c1"># טבלה זו מפרטת את פרטי האשראי עבור תרומות שבוצעו בכרטיס אשראי בלבד.</span>
<span class="c1"># היא כוללת מזהה פנימי (CreditDetailID), את מזהה התרומה שאליה היא שייכת (DonationID),</span>
<span class="c1"># מספר כרטיס, תוקף הכרטיס (Expiry) וקוד אימות (CVV).</span>
<span class="c1"># הנתונים בטבלה זו משמשים לצורכי הדמיה בלבד,</span>
<span class="c1"># ומאפשרים לבדוק אילו תרומות בוצעו באשראי ולבצע הצלבות נתונים לפי סוג תשלום.</span>

<span class="c1"># 5. טבלת CheckDetails (פרטי שיקים)</span>
<span class="c1"># טבלה זו מפרטת את התרומות שבוצעו באמצעות שיק.</span>
<span class="c1"># היא כוללת מזהה רשומה (CheckDetailID), מספר שיק (CheckNumber),</span>
<span class="c1"># תאריך פירעון (MaturityDate) וקישור לתרומה הרלוונטית (DonationID).</span>
<span class="c1"># באמצעות טבלה זו ניתן לעקוב אחרי שיקים שטרם נפרעו או לבחון את תזרים המזומנים העתידי של העמותה.</span>

<span class="c1"># 6. טבלת Receipts (קבלות)</span>
<span class="c1"># טבלה זו מרכזת את הקבלות שהונפקו עבור כל תרומה.</span>
<span class="c1"># היא כוללת את מזהה הקבלה (ReceiptID), מזהה התרומה (DonationID),</span>
<span class="c1"># השם שמופיע על הקבלה (NameOnReceipt), תאריך הפקת הקבלה (Date),</span>
<span class="c1"># ואופן המסירה (DeliveryMethod – לדוגמה: Email, SMS, Mail, Courier).</span>
<span class="c1"># הטבלה מאפשרת מעקב אחרי הנפקת הקבלות ואופן שליחתן לתורמים.</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=2ba6d6a5-896d-40fc-952c-c63c6de2b7fd">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [4]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># סטטיסטיקות של טבלת התרומות</span>
<span class="n">donations</span><span class="p">[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[4]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>count     50.000000
mean     206.500000
std       55.935914
min      100.000000
25%      170.000000
50%      202.500000
75%      247.500000
max      330.000000
Name: Amount, dtype: float64</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=0729167d-e28f-430d-9d9d-871ea9d9686a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [5]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># סה"כ תרומות בכל סוג תשלום</span>
<span class="n">donations</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"Type"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[5]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Type
Cash        2245.0
Check       2640.0
Credit      2035.0
Transfer    3405.0
Name: Amount, dtype: float64</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=e3f11b64-0a8b-4826-a153-fc3736372945">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># תרומה ממוצעת בכל סוג תשלום</span>
<span class="n">donations</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"Type"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[6]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Type
Cash        187.083333
Check       203.076923
Credit      156.538462
Transfer    283.750000
Name: Amount, dtype: float64</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=d999adbd-e8f0-4c5e-a3e8-2655dc964034">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [27]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># גרף של תרומה ממוצעת בכל סוג תשלום</span>
<span class="n">donations</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"Type"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span><span class="o">.</span><span class="n">plot</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'AVG Donation by Type'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">"Type"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">"AVG"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[27]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Text(0, 0.5, 'AVG')</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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"/>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=7daff379-5022-4679-94b2-42be38f3ade0">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># ניתן להסיק כי התרומות הגבוהות מתבצעות בהעברות בנקאיות</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=d4f6b9d2-a932-4a6f-89d1-3632ff4d1ef8">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># תרומה ממוצעת בכל איזור גיוס</span>
<span class="n">donations_with_regions</span> <span class="o">=</span> <span class="n">donations</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">donors</span><span class="p">)</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">regions</span><span class="p">)</span>
<span class="n">donations_with_regions</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"RegionName"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[7]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>RegionName
Central District      220.5
Jerusalem District    199.0
Northern District     206.5
Southern District     208.0
Tel Aviv District     198.5
Name: Amount, dtype: float64</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=ea0e5a0c-2f01-483f-8d1b-f2c2e8a7a2ce">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># ניתן להסיק כי במחוזהמרכז מתקבלות התרומות הגבוהות ביותר</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=5dd7a74f-29f0-458e-8679-e0feeaaa5406">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># סה"כ תרומות שגויסו ע"י כל אחד מהמנהלים</span>
<span class="n">donations_with_regions</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"Manager"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[8]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Manager
Amir Shalom      2065.0
Dan Cohen        1985.0
Ilan Peretz      2080.0
Moshe Levi       1990.0
Yossi Mizrahi    2205.0
Name: Amount, dtype: float64</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=50febbd0-6983-461a-9520-954aac8050ba">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># ניתן להסיק שהמנהל יוסי מזרחי גייס הכי הרבה תרומות </span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=ef0ae4f9-7b4a-4fc2-bf4f-13aefe7aabea">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># סה"כ תרומות לפי חודשים</span>
<span class="n">donations</span><span class="p">[</span><span class="s2">"Month"</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span><span class="n">donations</span><span class="p">[</span><span class="s2">"Date"</span><span class="p">])</span><span class="o">.</span><span class="n">dt</span><span class="o">.</span><span class="n">month</span>
<span class="n">donations</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"Month"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[9]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Month
1    6195.0
2    4130.0
Name: Amount, dtype: float64</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=7713775b-6e11-48fd-8154-cd6cdf9b2b07">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># ניתן להסיק כי בחודש ינואר גייסו יותר תרומות מחודש פברואר</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=d9667f80-d7fe-4920-a409-ec419b3e7c22">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [10]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># גרף להצגת התפלגות התרומות לפי סוג</span>
<span class="n">donations</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"Type"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">ascending</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">'bar'</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s2">"lightblue"</span><span class="p">,</span> <span class="n">edgecolor</span><span class="o">=</span><span class="s2">"black"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Donations by Type'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">"Type"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">"Amount"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">axis</span><span class="o">=</span><span class="s1">'y'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'--'</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.7</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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"/>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=bffd822d-39db-43fe-874c-0778eaadd8d9">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [11]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># גרף להצגת התפלגות התרומות לפי איזורים</span>
<span class="n">donations_with_regions</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">"RegionName"</span><span class="p">)[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">ascending</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">'pie'</span><span class="p">,</span><span class="n">autopct</span><span class="o">=</span><span class="s1">'</span><span class="si">%1.1f%%</span><span class="s1">'</span><span class="p">,</span> <span class="n">startangle</span><span class="o">=</span><span class="mi">90</span><span class="p">,</span><span class="n">shadow</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span><span class="n">explode</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mf">0.1</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">"Donations by region"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span> 
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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ODh06NBFxb18+XKGDx9OVFRUteOTJk2ivLy8xjBabXECHD9+HID4+Hj8/f157LHHeO+999i3b1+D4vH29q7xGnfccQdOp5PVq1e7rvnDH/7AzJkzKSsrc93Hvn37eOihh+r1OsOGDcPf39/12GKxsGzZMm666SY8PDyw2+2ur+uuuw6LxcKGDRsAWLVqFd27dycpKalam7fffnudr7t8+XKg6vt7rltvvRVPT0+WLVtW7XivXr2Ijo52PTaZTCQkJLi+30KIhpPkRoh6KCsrIy8vj4iICADy8vIACA8Pr3FtREQETqeTgoKCascDAwOrPTYajQBUVFQAkJ6ezqBBgzh16hRvvPEGa9asYfPmza75IGeua6i8vLzzxnnuvdQ3Tl9fX1atWkWvXr3417/+Rbdu3YiIiGDq1KnV5gadT20TssPCwmrE8te//pWSkhK++uorAN5++206dOjA2LFj63wNqPlvk5eXh91u56233kKv11f7uu666wDIzc11XVtbnPWZTJ6Xl4dOpyM4OLjacUVRCAsLq/P7DVXf84v99xZCyGopIeplwYIFOBwOhgwZApx9Q8rMzKxxbUZGBhqNplqvQX3MmTOHsrIyUlJSiImJcR3fsWPHRcd9JtbzxQkQFBTU4DaTk5P55ptvUFWVXbt2MXPmTKZPn47ZbObxxx+/4HNPnz5d41hWVpYr1jPi4+O59tpreeedd7j22muZN28ezzzzDFqttl4xnjvJGsDf3x+tVsvdd9993gnJHTt2dMVxoTgvJDAwELvdTk5OTrUER1VVsrKy6N+/f73iF0JcPOm5EaIO6enp/POf/8TX15f7778fgMTERCIjI5k1a1a14aqysjJ+/PFH1wqqhjjzZnympwSq3hA//PDDGtc25JP98OHDWb58uSuZOePzzz/Hw8PjkpaOK4pCz549ee211/Dz82Pbtm11PqekpIR58+ZVOzZr1iw0Gg1XX311teN///vf2bVrF/feey9arZbJkydfdKweHh4MHTqU7du306NHD/r161fj60xyNXjwYPbs2VNjyO2bb76p83WGDx8OwJdfflnt+I8//khZWZnrvBCi6UjPjRDn2LNnj2seRnZ2NmvWrHFt4jd79mzXJ3GNRsOMGTO48847GTNmDPfffz+VlZW89NJLFBYW8sILLzT4tUeOHInBYOD2229nypQpWCwW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6DXKysr47rvveOCBBxgzZky1npErr7ySxx9/vNr1OTk56PV6VqxYAVTvxbj99tuZOHFitettNhtBQUF8+umnF4wjJCSEsLAwEhISmDhxImvXriU4OJgHHnjAdc3ve2N++OEHkpOTMZvNBAYGMmLECMrKypg2bRqfffYZc+fOdfUKrVy5krS0NBRF4bvvvmPIkCGYTCa+/PLLWoel5s2bR79+/TCZTAQFBTF+/HgAhgwZwvHjx3nkkUeqTbgXjUN6boQQ52WxOcgrs5JfaiW3rJK8Uiv5ZZXkl9motDtwOFXsThXnb//1MGiZPra7u8N2G4fdyeEt2Rzeko1viJmkgREkXRWBybPl9eacsWjRIu666y7efPNNBg0aRGpqqmt4aOrUqfVu59tvvyUxMZHExETuuusu/vrXv/LUU0+hKAp33nknL730Es8//7zrTfzbb78lNDSUwYMH12jrzjvv5LbbbqO0tBQvLy9XnGVlZdx8880Nuj+z2cyf//xnHnnkEbKzswkJCal2PjMzk9tvv50ZM2Zw0003UVJSwpo1a1BVlX/+85/s37+f4uJiV1IVEBBARkYGAI899hivvPIKn376KUajkcWLF1dre8GCBYwfP55///vffPHFF1itVhYsWABASkoKPXv25E9/+hOTJ09u0D2JuklyI0Q7VWF1cDi7hINZJaTllZFbYiWvrJK8MutvSYyV0sqGfXoP9DS06+TmXEXZFayfncrWX9LoPrgDvUZEYfY2uDusGp599lkef/xx7r33XgDi4uL4z3/+w5QpUxqU3Hz88cfcddddAFxzzTWUlpaybNkyRowYwYQJE3jkkUf49ddfGTRoEACzZs3ijjvuQKOpOYAwevRoPD09mT17Nnfffbfr+htuuAEfH58G32OXLl0ASEtLqzW5sdvtjB8/npiYGADX8BVUJUeVlZWEhYXVaPfhhx929cTU5tlnn2XixIk888wzrmM9e/YEqpIkrVaLt7d3rW2LSyPJjRBtXKXdQWp2GYdOl5zzVcqJgnJkf/KmZ7U42LboOLtWnKDboEh6j4rG09fo7rBctm7dyubNm3n22WddxxwOBxaLhfLycjw8POps4+DBg2zatImUlBQAdDodEyZM4JNPPmHEiBEEBwczcuRIvvrqKwYNGsSxY8dYv3497777bq3t6fV6br31Vr766ivuvvtuysrKmDt3LrNmzbqoezyzgWRtQz89e/Zk+PDhJCcnM3r0aEaNGsUtt9yCv79/ne3269fvgud37NghvTJuIsmNEG1IWaWdTWn5bE8v5FBWCYeySzieV47DKVmMu9mtTnYuO8Ge1afoOiCcPqNjWkRBT6fTyTPPPFNrD4TJVL/4Pv74Y+x2O5GRka5jqqqi1+spKCjA39+fO++8k7///e+89dZbzJo1i27durl6MWpz5513MnjwYLKzs1myZAkmk4lrr7224TcI7N+/H6ia1/N7Wq2WJUuWsG7dOhYvXsxbb73Fv//9bzZu3EjHjh0v2K6np+cFz8vkYveR5EaIVsxic7DteAHrUvNYl5rLrpNF2CWRadEcNid7Vp1i368ZJF4RRt9rYvANrrt3pKn06dOHgwcPEh8ff1HPt9vtfP7557zyyiuMGjWq2rmbb76Zr776ioceeohx48Zx//33s3DhQmbNmuUabjqfAQMGEBUVxbfffssvv/zCrbfeisHQ8GG9iooKPvjgA66++urzrshSFIWBAwcycOBAnn76aWJiYpg9ezb/93//h8FgwOFwNPh1AXr06MGyZcv4wx/+UOv5S2lbXJgkN0K0InaHk50nC1l3JI91qXlsSy+g0u50d1jiIjgdKvvXZnJgfRYJ/UO57IaO+AQ1/yf9p59+mjFjxhAVFcWtt96KRqNh165d7N69m//+9791Pn/+/PkUFBTwxz/+scYS61tuuYWPP/6Yhx56CE9PT8aOHctTTz3F/v37ueOOOy7YrqIo3HHHHbz33nscOnTItaqqLtnZ2VgsFkpKSti6dSszZswgNzfXNWT2exs3bmTZsmWMGjWKkJAQNm7cSE5ODl27dgWqensWLVrEwYMHCQwMbNAy8qlTpzJ8+HA6derExIkTsdvt/PLLL0yZMsXV9urVq5k4cSJGo5GgoKB6ty0uTJaCC9HCpeWW8eHqo0z6dBM9n1nMze+u55Ulh1h/NE8SmzZAdaoc3JjFrGc2snHeUWzW5v0kP3r0aObPn8+SJUvo378/V1xxBa+++qprcm1dPv74Y0aMGFHrm/7NN9/Mjh072LZtG1A11LRz504GDRpUrz1w7rzzTvbt20dkZCQDBw6sVzyJiYlERETQt29fXnjhBUaMGMGePXtISkqq9XofHx9Wr17NddddR0JCAk8++SSvvPKKawhs8uTJJCYm0q9fP4KDg1m7dm294oCq5d7ff/898+bNo1evXgwbNoyNGze6zk+fPp20tDQ6derUaPv8iCqKqsqUQiFamtPFFn7amcG8nRnsOlnk7nDqLdDTwNanRroeb96wna8/+574hDjXMfVUKJReeK5Ce+blb+TK8Z1I6C8raIS4WDIsJUQLUVhu5efdWczbeYpNx/KRqTPtU2lBJUs+3seeVacYNCGB4Chvd4ckRKsjyY0QblRutbNk32nm7chg9eEcbA7JaESVzCNFfP/cZpKuiuDysXGYvVreHjlCtFSS3AjRzJxOlZWHspm9PYOl+05TYZPVEqJ2qgp712RwZGs2/cd0JHlwJBqtTJUUoi6S3AjRTMqtdr7fcpJP1x4jLa/c3eGIVqSy3M6v3x1m/9oMht3TlZCYhu/SK0R7IsmNEE0sq8jCzHVpfL0pnaIKm7vDEa1Y3qkyfnxxK71HR9P/+o5oddKLI0RtJLkRoonsOVXER2uOsmB3psylEY3G6VTZ+stx0nblMXxSV5lwLEQtJLkRohGpqsrS/dl8tOYoG4/luzsc0YblnSrlhxe20O+6WPpeG4tGU7NukhDtlfRptmGxsbG8/vrrLa6tc02aNIlx48Y1ervNrdLu4IsNxxn2yiomf75FEhvRLJwOlU0/HWPOK9sozq1wdzhCtBiS3NRDVlYWf/3rX4mLi8NoNBIVFcUNN9zAsmXLGvV1hgwZwsMPP9yobV7ItGnTUBQFRVHQ6XQEBQVx9dVX8/rrr1NZWVnt2s2bN/OnP/2pXu02JBF64403mDlzZr2uTUtLQ1EUduzYUa/rm4OqqszdcYrhr6ziqTl7OJZb5u6QRDuUmVrEt//dxMGNWe4ORYgWQYal6pCWlsbAgQPx8/NjxowZ9OjRA5vNxqJFi3jwwQc5cOBAs8ajqioOhwOdrnH+6bp168bSpUtxOp3k5eWxcuVK/vvf//LFF1+wcuVKvL2rxvMbe2twh8OBoigNqtPS0qxPzeP5X/a3qh2ERdtltThY+uk+ju/JY8idiRhM8uddtF/Sc1OHv/zlLyiKwqZNm7jllltISEigW7du/N///R8bNmxwXVdUVMSf/vQnQkJC8PHxYdiwYezcudN1ftq0afTq1YsvvviC2NhYfH19mThxIiUlJUDV8MyqVat44403XL0paWlprFy5EkVRWLRoEf369cNoNLJmzRpSU1MZO3YsoaGheHl50b9/f5YuXdrg+9PpdISFhREREUFycjJ//etfWbVqFXv27OHFF190Xff73php06YRHR2N0WgkIiKCv/3tb0BV79Px48d55JFHXPcBMHPmTPz8/Jg/fz5JSUkYjUaOHz9eY1jK6XTy4osvEh8fj9FoJDo6mmeffRaAjh07AtC7d28URWHIkCENvt/GcPh0CffN3MztH26QxEa0OIc3n+bHGVspypHtBkT7JcnNBeTn57Nw4UIefPBBPD1r1sLx8/MDqnpTrr/+erKysvj555/ZunUrffr0Yfjw4eTnn517kZqaypw5c5g/fz7z589n1apVvPDCC0DV8MyVV17J5MmTyczMJDMzk6ioKNdzp0yZwvPPP8/+/fvp0aMHpaWlXHfddSxdupTt27czevRobrjhBtLT0y/5vrt06cK111573iq6P/zwA6+99hrvv/8+hw8fZs6cOSQnJwOQkpJChw4dmD59uus+zigvL+f555/no48+Yu/evYSEhNRo+4knnuDFF1/kqaeeYt++fcyaNYvQ0FAANm3aBMDSpUvJzMw8b3xNJbvEwhMpu7jm9dUsP5DdrK8tREPkZ5Tx/fNbSN+X5+5QhHAL6be8gCNHjqCqKl26dLngdStWrGD37t1kZ2djNBoBePnll5kzZw4//PCDa66K0+lk5syZrqGeu+++m2XLlvHss8/i6+uLwWDAw8ODsLCaBfOmT5/OyJFnCxIGBgbSs2dP1+P//ve/zJ49m3nz5vHQQw9d8r136dKFxYsX13ouPT2dsLAwRowYgV6vJzo6mssuuwyAgIAAtFot3t7eNe7DZrPxv//9r1rc5yopKeGNN97g7bff5t577wWgU6dOXHXVVcDZobHAwMBav0dNpazSzvurj/LR6qOUy27CopWoLLcz/+1dXDmuE71H1V2BW4i2RHpuLuBMwfQzQyvns3XrVkpLSwkMDMTLy8v1dezYMVJTU13XxcbGuhIbgPDwcLKz69cD0K9fv2qPy8rKmDJlCklJSfj5+eHl5cWBAwcapecGqu79fPd96623UlFRQVxcHJMnT2b27NnY7fY62zQYDPTo0eO85/fv309lZSXDhw+/6Lgbk6qqfL0pnSEvreDNZYclsRGtjupUWZdyhMUf78VulZ9f0X5Iz80FdO7cGUVR2L9//wWXKzudTsLDw1m5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YmJizpvYAOzYsQOtVlst2Wwskty0c+fOu/Hy8Xcdz9ZFkcgO9wVWB3WqT53XKIrCtCEmpg05//LscxMWgFg/Tb3bXnufZ43jYxL0jEloufvcFCtaPvDTAS1/Jdel+uCqPIKKQ+m1UxKc1sDjisZLbs6s/FmwYAGRkdU3Jv39JFlPz+q/xxqNxjXEdIbtnJ3ctVotS5YsYd26dSxevJi33nqLf//732zcuJGOHTsyadIkcnJyeP3114mJicFoNHLllVdWG2L6fax9+/blq6++qnHu3MRAr6/+d+XMiqffH/v9qqf62r9/Px07dqz1XJ8+fTh27Bi//PILS5cu5bbbbmPEiBHV5jDV5vff298zm2suAmksLe9jpWhWF5p347zkdUWipflPcFdKNRXuDqPZPHdNLmlxUqahpdOFhWFKSGi09pKSkjAajaSnpxMfH1/tKyrqwgsmgoODyczMrHbs9/NFFEVh4MCBPPPMM2zfvh2DwcDs2bMBWLNmDX/729+47rrr6NatG0ajkdzc8/eC9+nTh8OHDxMSElIjVl/f5tneYPny5ezevZubb775vNf4+PgwYcIEPvzwQ7799lt+/PFH8vPzgarEy+Fo+OKJ5ORknE5njXlQZxgMVb3wF9O2JDft3Jl5N5by6gUTKzUe5Ooi3BSVaAp79H4s8Wj5hTEblUbhqfGF5IT5132tcBuf0XUPcTSEt7c3//znP3nkkUf47LPPSE1NZfv27bzzzjt89tlnF3zusGHD2LJlC59//jmHDx9m6tSp7Nmzx3V+48aNPPfcc2zZsoX09HRSUlLIycmha9euAMTHx/PFF1+wf/9+Nm7cyJ133nnBHoo777yToKAgxo4dy5o1azh27BirVq3i73//OydPnmycb8g5KisrycrK4tSpU2zbto3nnnuOsWPHMmbMGO65555an/Paa6/xzTffcODAAQ4dOsT3339PWFiYax5MbGwsy5YtIysri4KCgnrHEhsby7333st9993HnDlzOHbsGCtXruS7774Dqoa1FEVh/vz55OTkUFpa/79fktyIavNuzpVuSHRTRKIpTA2JxqG03H13mkqlXuWpCRZK/LzcHYo4D+/RoxulHafTie63iuL/+c9/ePrpp3n++efp2rUro0eP5qeffjrv0MsZo0eP5qmnnmLKlCn079+fkpKSam/6Pj4+rF69muuu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HDt2rM52a4v7XGZz4y/R1hsM9LhiKJUV5TWWhefqIzipj2v01xR1mxbSAaci+9q4w+eX57Gxn+yBU1+Bf5iE1ksmZIvmdcn73CQlJVFWVub6//T0dE6cOOE6v2/fPoqKiujataouUXBwcI35Hjt27Kj22GAw4HA4GhxLnz59OHjwIPHx8TW+NM1UL6aiooIPPviAq6++muDg4FqvURSFgQMH8swzz7B9+3YMBgOzZ88GLv7eoapXa9myZec9f7FtJ/ToT2BIOAU5WTXO7fS4Sraqb2Zfe8dy2CD1o9zplZF5HE6QHpy6aP38CLj7bneHIdqher/j5+XlMWzYML788kvXvJrvv/+eGTNmMHbsWABGjBhBjx49uPPOO9m2bRubNm3innvuYfDgwa4hlWHDhrFlyxY+//xzDh8+zNSpU9mzZ0+114qNjWXjxo2kpaWRm5tb7x6Up59+ms8//5xp06axd+9e9u/fz7fffsuTTz5Z39tssOzsbLKysjh8+DDffPMNAwcOJDc3l3fffbfW6zdu3Mhzzz3Hli1bSE9PJyUlhZycHFfyFxsby65duzh48CC5ubkN6tWaOnUqX3/9NVOnTmX//v3s3r2bGTNmuM7HxsayevVqTp06RW5ubr3b9fDyodtlgyktzK/xb1GkC+a4QVZONZcyVcM7Aaa6LxRNbtrYArIiA9wdRosW8Mf70NTR4yxEU2jQaqnLL7+c1157jauvvpru3bvz1FNPMXnyZN5++22gqkdizpw5+Pv7c/XVVzNixAji4uL49ttvXe2MHj2ap556iilTptC/f39KSkq45557qr3WP//5T7RaLUlJSQQHB5Oenl6vGEePHs38+fNZsmQJ/fv354orruDVV191TdxtComJiURERNC3b19eeOEFRowYwZ49e0hKSqr1eh8fH1avXs11111HQkICTz75JK+88grXXnstAJMnTyYxMZF+/foRHBzM2rVr6x3LkCFD+P7775k3bx69evVi2LBhbNy40XV++vTppKWl0alTp/P2Kp1Pt35X4RsUQmEtvTe7PAbibD2bXbdqL4R0pUhTXveFosnZdCpP3lpGUYBMlK2NNjCQgDvvdHcYop1S1N9PgBHiPNYuTGHVT7OI7twNjbb6EuT+pUvoXLnLTZG1D4d03kzoEIRdubhhS9E0OhQaefZzJ+ayCneH0qKETJlC4H1/cHcYop2Sj9ui3npcMYTA0AjyszNqnNvjcSX2+u8sIC7C1JCOkti0QCf9KplxqwGbQV/3xe2ENjgI/zukQKZwH0luRL15+wXQ+6pRlBYV1Fg5VaHx4pBUDG8yP3lFscdY6O4wxHnsDS/jg7E+OJtp4UJLFzR5MhqTzA0T7iO/iaJBul92NSGRMeRmnqxxbp/5MqyKwQ1RtW2VqsIrAbKUtqVbFV/ED6OC2v3qQX1MNH4TJ7o7DNHOSXIjGsTDy4e+V1+DpbwEu81a7ZxVY5ayDE3glaAu5GnL3B2GqIcfeuezakD73gMn7Mmn0BjkQ45wL0luRIMl9R1IeHQ8ORknapzbb+5HqUZWjzSW4xoPfvC21n2haDH+NziP3d3bZ4LjPXo0XoOucncYQkhyIxrOaPag3+BrsVktWCst1c45FD1bPBu3BER7Ni00HptS/72ORMvw7PV5pMcGuTuMZqWYzYQ+8bi7wxACkORGXKTEXpfTIa4LORk19yDKMMRx3JDghqjalmXmcLbIJOJWyamBp8YXkxfi5+5Qmk3wQw+ir2dRXiGamiQ34qLoDUb6Db4G1emksqLmpnJbPYdhVYxuiKxtcKjwfHAA1CzVJlqJCqOTpyZUUurT9nfo1cfFEXCvFMcULYckN+KidU7uT8cuPTh98liNYqgWjSc7PAa5KbLW762ARE5rS9wdhrhEuV42np2gwWpq24l++LSpKDrZ50q0HJLciIum1ekYMHo8Zk9vivKya5w/YuxBti7CDZG1bqc1Rr7ylc362orUoArevNkDh05b98WtkPcNY/C87DJ3hyFENZLciEsS2TGBPoNGU5B7Gvvvi3wqCps8R+Ggbf5RbyrTQhKxKLJCqi3ZFF3CF9cFoCpta5xR8fQk7LHH3B2GEDVIciMuWb/B1xIVl8jpk8dqnCvWBbLf3N8NUbVO641BrDUVuTsM0QR+7lbAL0NC3B1Gowr5x/+hC2pfq8JE6yDJjbhkZk8vBowej6IolBYX1Di/x3w5xRp/N0TW+vwnJAxVae973LZdM6/IY3OftrEHjnnAAPxvl/pRomWSquCiUaiqyqLvPmLb6kVEJ3RH87saOyG2E4wo/s5N0bUOH/rG82ZAyxqOypmfQ/HWYiozK1H0Ch7xHoTdFoYx/OwEWVVVyZ6TTcGqAhxlDsxxZiLuicAUeeHaQkWbi8ienY0124ohxEDozaH49D27AWThukKyfshCrVTxH+RP2MSzy4ytOVbSXk6j07ROaM2tb9jzuR/8iT+c4+4wLp6PD51/XiC9NqLFkp4b0SgUReHKkeMICutQ69432fooDpj6uiGy1qFQ0fOxX8v7dSw7UEbAsADinooj9tFYcELay2k4K52ua3J/ziVvUR7hd4XTaWon9L560l5Kw1Fx/knR5UfKOfHuCfwG+BE/PR6/AX6k/y+d8tSqbQXsJXZOfXqK8AnhxPwjhoK1BZTsOLt6LOPzDEJvDW2ViQ3A1HGFZEUGuDuMixb54guS2IgWreX9NRWtlm9AMFeMHIfVUo6lomYtpO0eg8jVySZftXkmpAtlGkvdFzaz2H/G4j/IH1OkCXO0mcg/RmLLs1GRVgFU9drkLc4j+IZgfPv5YupgInJyJM5KJ0Ubzj93KHdxLl7dvAgeE4wxwkjwmGC8unqRtzgPqOqZ0Zq1+F7ui0ecB55dPbFkVH1/CtcXougUfPv5Nv03oInYdCpP3VpOsb+3u0NpMNNN4/AZOtTdYQhxQZLciEbVrd9VdE7ux+kTNfe+URUta73GyOZ+v7PDEMByc+vY0+ZMb4zWs6rHxJZjw15kx6v72arlGr0Gzy6elB+pubnjGRVHKqo9B8Ar2cv1HGOoEafVScXxCuyldiqOVWCKMmEvtZM9O5vwu8Ib+9aaXZHZzrSJTiweZneHUm+OiHBipk1zdxhC1EmSG9GotDodA6+5BS9ff/KzM2ucL9P6ssFrtBsia7mmhUTiVJx1X+hmqqqS9XUWHgkemDpUzaexF9kB0PlU38BN56NznauNvch+wedoPbV0mNyBkx+e5Oj0o/gN8MM72Zusb7MIGBGALdfGkaePcPjfhyna3HpXl530q+SlWw3Y9Xp3h1Inp1ZL3NtvozHKhxPR8klyIxpdaIdYLhs6hrLifCzlNYenTho6c9DU2w2RtTxf+XQkVd863pwzv8jEcsJC1J+jap78/fYt9VmmUMdzfPr60Pm/nUmYkUDoTaGU7i+l8mQlAYMDOPHuCcLvCCf6oWhOfXIKe/H5E6mWbndEGR+M9cGpadl/jv0eegiPpCR3hyFEvbTs3ybRavW9+hq69hlIVnoqDkfNiaXbPQaTp20bS2IvVpmq4X/+reNTcMYXGRTvKKbj4x3RB5ztZdD5VvW+/L6Xxl5id52rjc63Zs/OhZ7jtDnJ/CKTiHsjsGZbUR0qnl08MYYbMYYZXRORW6uVnYv4cWRQvXJCt+jZk8gH/uzuKISoN0luRJPQ6fUMufEOQqPiyDp+pMZ5p6LlV+8b2vX8m+dCulKsadlvyqqqViU2W4vpOKUjhmBDtfP6YD06Xx2le0tdx5x2J2UHyvCI9zhvu+Z4c7XnAJTuKT3vc3Lm5eCV7IU51ozqVOGcUTzVXv1xa/V9n3xWX9nyEn6Hlxfxb7/l7jCEaBBJbkST8Q0IZujYO9AbjBTkZNU4X6b1ZaPnKDdE5n4HdD4s8GzZiQ1UDUUVrisk6s9RaEwabIU2bIU2nNaqbEJRFAJHBZLzU9V+OJaTFk59dAqNUYPvFWdXM5384CRZ35/9GQgaGUTpnlJyFuRQmVFJzoIcSveVEjgqsEYMllMWijYVETq+6o3fGG4EBfJX5VOyo4TKzErMca1nUu6FvDMkj73dWk6C49Rq6fD22+iDg90dihANIpv4iSa3fskcVs6bRWhUR0xmzxrn+5UuI6FyR/MH5kYTI3uw11Do7jDqtGfSnlqPR/4xEv9BVbtOuzbxW/nbJn6dzETcHeGadAxw9PmjGIIMdJjcwXWsaHMRp388jS3HhiHEQMjNITWWd6uqyrFnjxE0JgifXmc3+CveUUzmF5moNpWQm0MIGNx694z5PY0DXvrWj6jjue4OBfOUR4m97z53hyFEg0lyI5qczWplwZfvsG/bOqLjk9Boq2+8plHtDC/+nmB7hpsibF5zvKJ5Sj4IiwvwqNTw6hdmAnLcN9nces1oer7+utteX4hLIcNSosnpDQaGjL2T0A6xZKan1jjvVHSs8h7XLupPVaoKrwXU7L0S4lzlRidPT7BR5u2en5Xi+Hi6vfyyW15biMYgyY1oFn6BIQy58Q50Oj2FuadrnLdqzKzwGU+Fcv5JqG3BS8FdydfWXB4vxO9le1t5boIGq6l5J92X+vuT8P576HTnX+0mREsnyY1oNnFde3H58Bspys+hsqLmZNoyrR+rvcdhp23+UT2u8SDFq+WVWBAt1+HgCt4e74lD2zw1tCxGI+FvvoF/ZGSzvJ4QTUWSG9FsFEWh/9DrSex1BZnHj2C32Wpck6cPZ6339Thr7PDW+j0dGo9Nab2bzQn32BBTzFfXBaAqTfs7YddoMD/5bzr079+kryNEc5DkRjQrvcHAyJsnEZ3QjVPHDuKsZYO/U4Z4tnoOc0N0TWeJRwTbjIXuDkO0UvO7F7Do6pAma18FrPfcTZdbb22y1xCiOUlyI5qdt18A10yYTEhEDKeOHapRYBPgsKkX+0z93BBd47Or8EKQf81yA0I0wCcD8tjau2n2wCkYNozeU6Y0SdtCuIMkN8ItgsI6MPq2P+LtF0BW+tFar9nhcTXHDYnNHFnjezMgkWxt66j6LVq2F0flkhrfuPsIZPXvR/9XX0HTwmtbCdEQ8tMs3KZDpy6MuPletDoduVkna16gKKz3uobTug41z7USWRojX/vWHHoT4qJoFKbeVEh2eONsm3AiKYm+b7yBwWSq+2IhWhFJboRbJfS4jMFjJlJZXk5Rfk6N805Fx2rvceTqwt0Q3aWbGpKIRbG6OwzRhlh1Kk9OqKDY3/uS2knr2JEer72KT0Db2d1ZiDMkuRFu12vgCK4YOZaivGzKSmruyGrTGFnucwvZuta1PHWtKZj1JvftMCvarkKznem3qVg8Lq6m1tHISOKee5awmJhGjkyIlkGSG+F2iqIwYNRN9B44kpxTx2vdA8euGFjhczNZumg3RHhx/hsciqpIdRPRNNIDLLxyqxG7Xt+g56WFhxM9/RkSe/duosiEcD9JbkSLoNXpGDL2Trr0GUDG8cPYrDWHchyKnlU+48jQxzZ/gA30vl9nTuqK3R2GaON2RpTy0Y0+OOs5Gfh4aCjh058heeDAJo5MCPeS5Ea0GEaTmVG3/IFOXXtz8ugBbNbKGtc4FD2rvcdySh/nhgjrJ1/R84lv3dcJ0RiWJxQxZ0RQndelBwcTPPVpel51VTNEJYR7SXIjWhQvX3+uu/MB4rv14dTRg1gra5YrqJpkfCPphs5uiLBu00O6UK6pmZgJ0VS+6ZvPr1ecfw+c48HBBDz9FH2GDkVp4p2OhWgJJLkRLY6PfyDX3/kAnZP7kXHsEFZLRY1rVEXLWq8xpLWwfXC2GgJYYZY9bUTze3NoHvuSaiY4B8PD8X/y3/QbMUISG9FuSHIjWqQzPTiJvS7nVNqhWicZq4qG9V7XcdSY5IYIazc9JBKn4nR3GKKdmj4mj1PRgUBVSYUdMdGEPPpPLhs1ShIb0a4oam173wvRQpSXlrDw2w85sG0dYTGdMJk9a16kqvQuX0VXy9bmD/AcX/jEMSNQCmMK9/Ko1DBjppGj/sF0fuABBl5/vSQ2ot2R5Ea0eBVlpSz+/mP2bl5DWHQnTB61JDhAnGUP/cuWoqX5dwQuUbSMjo6nRFNzCE2I5qS367hyVyy3Db2XQTfeKGUVRLskyY1oFSoryln8/cfs3riK0KiOmD1r3501yHaKq0vmYlKbN8l4Irg7871k6bdwL0+Lkav3JnDTtXdz+ejRktiIdkuSG9FqVFoqWPrjTHauX05IZAweXj61XufhKGZwyWz8HbnNEtd+nS+3dwjAoUgNKeE+AcWeDD3cjXG3/YGeAwfKUJRo1yS5Ea2KtdLC8jlfsGPtUnwDgvENDKn1Op1q5cqSn4mypTZ5TLdF9mC/obDJX0eI8/E+qjC2cBDjJv0/2XlYCCS5Ea2Q3WZj47Kf2LBkDhqdjpDImNo/paoqPct/pZtlU5PFkuIVzdTgJmteiAtSVIWQE4HEpvrz+KPTie/W3d0hCdEiSHIjWiVVVdm3dS0r5n5JWXERkR0T0Gi1tV4bW7mPy0sXN/pE4wpVw+iYRAq0ZY3arhD1YXaaCU8N57LIy5g0fhKRoa2rsKwQTUmSG9GqnUw9wOIfPiXrxFEiOyagNxhrvS7Qlsmg0nl4OEsb7bWnByXxvXfjtSdEfQVXBhN8JJiB3Qdy97i78ffxd3dIQrQoktyIVq8gJ4slP3zCkT3bCOkQe96JxnqnhcvKlhBjPXTJr3lM68nNUaHYFNnXRjQfRVXoWNgRn1M+jBwwkluvvRWzyezusIRocSS5EW2CpbyMlT/NYsfapfj4B+EXdP46Ox0r99K3bDkGtWbl8fq6O6IHO4yFF/18IRrK7DQTkx5DkCOIG4bdwOhBo9GeZyhWiPZOkhvRZjjsdjatmM/6xbNB0RDaIfa8y2E9HUVcWfoLIfZTDX6dhR4RPBqiA1lpK5pJiDWEwEOBJEQkMPH6iXRPkInDQlyIJDeiTVFVlQPb17N87peUFOQTHhOP3mCo9VpFdZJUsYnuFevRUr96UHYVRsUkkaOVuTai6SmqQseijnif8ObKXlcy8fqJBPoHujssIVo8SW5Em5Rx/Agr580i7cAuAkIj8PEPOu+1AfYsriz5GV9nQZ3tvhzQhc98axbxFKKxBTgCCDseRoAawJhhYxg1cBR6vd7dYQnRKkhyI9osS3kZG5bMYduvi3E6HYRGdTrvHAWtaqNP2So6V+48b3sZGhM3RkdSqdiaKmQh0Kk6upR3gSPQKaqTDEMJcREkuRFtmqqqpO7dxqr533L6xNELrqYCiLAepV/ZMrycNetETQ7vwQZTYRNGK9q7CEcEMadjqMir4IpeV8gwlBAXSZIb0S4UF+Sx5ufv2LNpNUazB8ER0eedbKxVbXQv30AXyxbXXJw1phAeDDOjKvLrIhqfSTXRq6IXtjQbJqOJG4bdIMNQQlwCSW5Eu+FwONizaTVrF/1AYW42ETHxGC6wR0hp5m76WVbRx6eSa6K6c0onVb9FI1MhzhFHh9MdKMgtIKFjAreMvkWGoYS4RJLciHYnJyOdlfNmcWTvNteeOL/vxbHb7aSs+plSo5EbBybypc8eKpQKN0Us2iIfpw89y3pScrwEbw9vRg4cycirRuLl4eXu0IRo9SS5Ee2SzVrJ5pU/s3nFAirKSgjt0BGj2cN1fvv+Haw/fpjLrxhGYHAoduzs0+3jgO4ADqVxa1SJ9sWoGkmyJeFxyoPS0lJ6dOnBTSNvonNMZ3eHJkSbIcmNaNdOHTvEukUppO7bjtHsSXB4FOWWCr7/dSFeoRH07391tevLlDJ26HaQrkt3U8SitdKrerrYuxBZFElGRgYhASFcN+Q6Bl82GIO+9r2YhBAXR5Ib0e7ZbTb2bvmVjUvnkpN1kkN5pzlaXsrQYWMwnWdOTo4mh9263ZzWnm7maEVro1W1xNvj6VLZhayMLOx2O5f3vJyxI8YSERLh7vCEaJMkuRHiN8X5uWxY9hNvf/8hTi8fevfoX2dRwhxNDnt1e8nUZjZTlKK1UFSFOEcc3WzdsBRayMzOJCYihrEjxtI/ub/UhRKiCUlyI8Q5VFVl78HdLFy7mN0Hd6PX64kOj0an013weXlKHnv1ezmlbXitKtHGqBDliKKHvQfOYicZWRl4e3ozsO9ArhtyHQG+Ae6OUIg2T5IbIWphs9nYvHszP6/6maMnjhLoH0hYUNh598Y5o0ApYK9+Lyc0J6SwZjujqAqRzki62bphKDVwIvMEJqOJfsn9GDlwJB07dKzz50cI0TgkuRHiAkrKSli5cSVL1i4htyCXIP8gQgJD0Gg0F3xeoVLIXt1eTmhPyMZ/bZxe1dPJ3onOjs5oK7SkZ6Sj1Wjp0aUH1wy6hsS4RElqhGhmktwIUQ+nc0+zZssaVm9eTW5BLoF+gYQGhdaZ5BQrxRzQHeC49jh2xd5M0Yrm4O30JtGeSEdHRxxWBycyT+BwOEiKT2L0oNH0SOxR58+HEKJpSHIjRAPk5Ofw69ZfWb1pNafzThPgG0BoUGidk0Nt2EjXppOqSyVPk9dM0YpGp0K4M5xEeyJhzjDsNjsnT5/EYrGQ0DGBUVeNom+3vnXO0RJCNC1JboS4CHkFeazdtpZVm1aRmZuJn7cf4cHh9VoBU6AUkKpLJU2bhk0qjLcKOlVHR0dHEuwJ+Kg+lFeUk5mTSaW1ktjIWEZdNYrLe16O0WB0d6hCCCS5EeKS5Bfls377elZsWEFGdga+3r6Eh4Sj09b9yd2OnRPaE6RqU8nR5jRDtKIhFFUhzBlGtCOaKEcUOlVHYXEhWTlZ6LQ6OsV04ur+V9O3e188zZ7uDlcIcQ5JboRoBIUlhWzYsYHl65eTkZ2BXqcnLDgMLw+vek0mLVKKSNWmkq5LlxpWbqSoCsHOYGIcMUQ5ojBixOFwkJ2XTX5hPj7ePvTs0pMBfQaQ1ClJhp+EaKEkuRGiERWXFrPzwE7WbVvHkfQjlFeUE+AbQHBAcL3eCFVU8pV8TmlPcVJ7kiJNUTNE3c6pEOQMItoRTbQjGjNVGzdaKi1kZGdQYakgNCiUgb0H0r9Hf6LCo2T1kxAtnCQ3QjQBp9NJ6olUtu/dzsZdG8nOzUan0xESGIKPl0+93xxLlVJOak5ySnuKHE2OLCtvLCoEqAFEOaKIccTgqVYNKzmdTgpLCsnOzUaj0dCxQ0cG9R9E32598fX2dXPQQoj6kuRGiCZWUlbC7oO7Wb9jPYeOHaK0rBQ/Xz9CAkLQ6/X1bqeSSjK0GZzSniJTkylLyxvI2+lNqDOUUEcooc5QjFRN/lVVlaKSInLyc7DarPh5+9E1visDeg+ge0J3KWopRCskyY0QzURVVY6dPMaOfTvYsGMDmblV9agCfAMI8A1oUKLjwEGeJo9cTa7rq1KpbKrQWyVPpychzhBXQuOBh+ucqqoUlxaTW5CLpdKCj5cP8THx9O3Wl6T4JIIDgmXoSYhWTJIbIdygrOL/t3fvsU3V/x/Hn6fd1pa2W7fB1m2MFb4/xr7AZCMj/oEXQIwTiUqCYEIyJwl/iMRLIGhIUBTDJTiJg+AlcosmkikEDJFF7omXqEEWEBAHOsxwjB8yduvWbu35/bEfDXVcNhgw6+uRnPT0nE/fO+f8c177nE/7aeXnkz/zc/XPHKs+xoVLFwiHwiS6E0n1pN5wws6raTaao8JOo9H4r3mMZZgGLtNFSjilK8yE03GZrqg2pmnS4m/hwsULtLa14na6GTp4KEX5RYz8n5FkDMpQoBGJEQo3IndZi7+FU2dOcfK3k1SdqKL+r3oCwQBOh5MUTwpup/umbroddHDRcpELlgtctFykyWii1WglZIRuw1ncOXbTjifsISmchMf04Al7SDQTiaP7gO3Ozk4amxu51HyJtkAbLoeLIZlDGJc/jv/+578aHCwSoxRuRPqRYEeQmtoaqmuqOXz8MLX1tTS3NpMQn4An0YPb6cZus990fRMTv+Gn2WimxWih2Wim2dK13mK09JvgYzEtOEwHA8wBJJqJXWHGTMIT9kTGylxNKBSiqaWpK8y0tWGxWEhyJzEkYwijc0eT9588cjJzNC2CSIxTuBHpp8LhMGfrz1J9ppqjvxzlt9rfaG5pJtgZxGJYcDvduF1uXANcfXKzvhx8WowW2o12ggTpMDoIEiRoBOmgg6ARvd5BB2EjHKlhmAYGBhYsGESvW8yu1zjisJk27KYdGzZsZtdyOcw4TAd27Bg9mFY9HA7T1NpEY1Mjrf5WDItBojORzPRMRg0fhS/LR05WDsmJybd8fUTkn0PhRuQfosXfwp/1f1JbXxvp3WloaqDF3wIm2O12El2JuJ3uOzoNQIhQJMTcTh2dHfjb/Pjb/LS2tRLsCAKQ6EwkbWAa+cPz8WX78GX6SPGk6HGTyL+Ywo3IP1QoFKL+r3rO1p+l9lwt1TXVnK0/S1NLEx2dXXNWxcfFY7fZcdgdOGwO7DZ7j+a/upvC4TD+9q4A42/z09be9YvNVosVp8OJ0+kk25tNTmYO3oFefIN9pKWmKcyISITCjUgMaW5t5uy5s9T/VU9DYwN1/1vHn+f/pKmlibb2NtoCbWB2PYK6MvjEx8UTFxdHnLVrsVgstyUshMNhgh1BOjs7CXYECXQECAQDkW2XH0UNcAxggGMAGYMyyMnMIX1gOoNSBjEoZRCpntR+H9BE5O5SuBGJcaZp4m/309DYwMXGizQ0NnQLPh2dHXR2dtIZ6iQUChEKh6LGvJimiWExiLPGYbVYMTExzb8t/7/tcnjCBAwidUxMDMMgPi6e+Lh4EuITsNvtpCSmMDB5IKnJqbidbgYmD4wEGc2yLSI3Q+FG5F/scvBpb2+nPdhOe6CdQDBAW6CNQCBAe7A98upv89Pib6Et0IbVYu1arNd+tVgsWCwWbPE2HHYHA+xdvTEOuwOnw4nL6cLpcOqbSyLS5xRuREREJKboXyYRERGJKQo3IiIiElMUbkREgNLSUp588sm7fRg3xTAMtm/f3ud1J0yYwEsvvdTndUVuN4UbEelXSktLMQyDFStWRG3fvn17n3w9vaamBsMwqKqquuVat9Pl62AYBvHx8aSnp/Pwww+zYcMGwuFwVNu6ujoeffTRHtXtTRDatm0bS5cu7VHbAwcOYBgGly5d6lF7kdtJ4UZE+h273c7KlStpaGjo07rBYLBP691IKBTqFkR6o7i4mLq6Ompqati1axcTJ07kxRdfZOrUqXR2dkbaeb1ebLa++9p8R0fXj0CmpKTgdrv7rK7InaJwIyL9zuTJk/F6vSxfvvy67bZu3cqoUaOw2Wz4fD7Kysqi9vt8Pt566y1KS0tJSkpizpw5DB06FIDCwkIMw2DChAlRn3n77bfJyMggNTWV559/PnKjh65wtHDhQrKysnA6ndx7770cOHAgsn/Tpk14PB527tzJyJEjsdlsnDlzBp/Px7Jly5g9ezZut5shQ4bw4Ycf3vA62Gw2vF4vWVlZjB07lkWLFrFjxw527drFpk2bIu2u7I0JBoPMmzePjIwM7HY7Pp8vch19Ph8A06ZNwzCMyPslS5ZQUFDAhg0bGDZsGDabDdM0uz2WCgQCLFy4kOzsbGw2G8OHD2f9+vXU1NQwceJEAJKTkzEMg9LS0huen8jtonAjIv2O1Wpl2bJlrFmzhtra2qu2OXToEDNmzODpp5/m6NGjLFmyhMWLF0fd9AFWrVrF6NGjOXToEIsXL+aHH34AYM+ePdTV1bFt27ZI2/3793P69Gn279/P5s2b2bRpU1S9Z599lm+++YYtW7Zw5MgRnnrqKYqLi6muro608fv9LF++nI8++ohjx46RlpYGQFlZGUVFRRw+fJi5c+fy3HPP8csvv/T62kyaNIkxY8ZEHfeVysvL+eKLL6ioqODkyZN88sknkRDz448/ArBx40bq6uoi7wFOnTpFRUUFW7duveYju5KSErZs2UJ5eTknTpzg/fffx+VykZ2dzdatWwE4efIkdXV1vPvuu70+N5G+Ene3D0BE5GqmTZtGQUEBr7/+OuvXr++2/5133uGhhx5i8eLFAOTm5nL8+HFWrVoV1WswadIkFixYEHlfU1MDQGpqKl6vN6pmcnIya9euxWq1kpeXx2OPPcbevXuZM2cOp0+f5tNPP6W2tpbMzEwAFixYQGVlJRs3bmTZsmVA1yOddevWMWbMmKjaU6ZMYe7cuQC88sorrF69mgMHDpCXl9fra5OXl8eRI0euuu+PP/5g+PDh3HfffRiGQU5OTmTfoEGDAPB4PN3OPRgM8vHHH0fa/N2vv/5KRUUFu3fvZvLkyQAMGzYssj8lJQWAtLQ0PB5Pr89JpC+p50ZE+q2VK1eyefNmjh8/3m3fiRMnGD9+fNS28ePHU11dTSgUimwrKirq8d8bNWpU1LxVGRkZnD9/HoCffvoJ0zTJzc3F5XJFloMHD3L69OnIZxISErjnnnu61b5ym2EYeL3eSO3eMk3zmoOrS0tLqaqqYsSIEbzwwgt89dVXPaqZk5NzzWADUFVVhdVq5cEHH7ypYxa5k9RzIyL91gMPPMAjjzzCokWLuo3huNoN/mo/uO50Onv89+Lj46PeG4YRGRAcDoexWq0cOnSo28SdLpcrsu5wOK4aPK5Xu7dOnDgRGTv0d2PHjuX3339n165d7NmzhxkzZjB58mQ+//zz69a80XVyOBw3dawid4PCjYj0aytWrKCgoIDc3Nyo7SNHjuTrr7+O2vbtt9+Sm5t73VnDExISAKJ6d3qisLCQUCjE+fPnuf/++3v12b60b98+jh49yssvv3zNNomJicycOZOZM2cyffp0iouLuXjxIikpKcTHx/f63AHy8/MJh8McPHgw8ljqSjd7XUVuB4UbEenX8vPzmTVrFmvWrInaPn/+fMaNG8fSpUuZOXMm3333HWvXrmXdunXXrZeWlobD4aCyspLBgwdjt9tJSkq64XHk5uYya9YsSkpKKCsro7CwkAsXLrBv3z7y8/OZMmXKLZ3n1QQCAc6dO0coFKK+vp7KykqWL1/O1KlTKSkpuepnVq9eTUZGBgUFBVgsFj777DO8Xm9kHIzP52Pv3r2MHz8em81GcnJyj47F5/PxzDPPMHv2bMrLyxkzZgxnzpzh/PnzzJgxg5ycHAzDYOfOnUyZMgWHwxHVoyVyJ2nMjYj0e0uXLu32yGns2LFUVFSwZcsWRo8ezWuvvcabb755w68gx8XFUV5ezgcffEBmZiZPPPFEj49j48aNlJSUMH/+fEaMGMHjjz/O999/T3Z29s2c1g1VVlaSkZGBz+ejuLiY/fv3U15ezo4dO67ZO+VyuVi5ciVFRUWMGzeOmpoavvzyy8js62VlZezevZvs7GwKCwt7dTzvvfce06dPZ+7cueTl5TFnzhxaW1sByMrK4o033uDVV18lPT2defPm3drJi9wCzQouIiIiMUU9NyIiIhJTFG5EREQkpijciIiISExRuBEREZGYonAjIiIiMUXhRkRERGKKwo2IiIjEFIUbERERiSkKNyIiIhJTFG5EREQkpijciIiISExRuBEREZGYonAjIiIiMUXhRkRERGKKwo2IiIjEFIUbERERiSkKNyIiIhJTFG5EREQkpijciIiISExRuBEREZGYonAjIiIiMUXhRkRERGKKwo2IiIjEFIUbERERiSkKNyIiIhJTFG5EREQkpijciIiISEz5P9CPKI2f7btxAAAAAElFTkSuQmCC"/>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=cd0682ce-4a64-44b9-b6a8-e05116505670">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [24]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># התפלגות אמצעי תשלום לפי אזורים במטרה להבין באיזה איזור יש צורך לעודד שימוש באשראי</span>
<span class="n">sum_by_region_and_type</span> <span class="o">=</span> <span class="n">donations_with_regions</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s2">"RegionName"</span><span class="p">,</span> <span class="s2">"Type"</span><span class="p">])[</span><span class="s2">"Amount"</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span><span class="o">.</span><span class="n">unstack</span><span class="p">()</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">6</span><span class="p">))</span>
<span class="n">sb</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">sum_by_region_and_type</span><span class="p">,</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">fmt</span><span class="o">=</span><span class="s2">".0f"</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">"YlGnBu"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">"Donation by Region and type"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">"Type"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">"RegionName"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[24]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Text(70.72222222222221, 0.5, 'RegionName')</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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cW1lm2uZVcga/jNjxgyrukajMccZ9GbNmvHLL7+YA81rPv/8c1xdXfN9+cYvvvjC4vHChQtJT0+3+sKjF154AScnJzp16sT+/ft59dVX83xOo9HIhx9+SHJyMiNHjgSgZcuWODg4cOjQIerUqZPtBlnPZWBgIAsXLrRo8/jx42zcuPG2575b99dgMFj8bEDWG85Tp07lqb17770XZ2dnq+dr48aNOR52daufQ2dnZ1588UXmzJnDxIkTqVGjxk2HNt3uZyanz6WIFD5l7EWkyNi9e7d5/G5cXBy//vors2bNwt7eniVLllCyZEkgK2M8btw4OnXqxCOPPEKPHj1ISUlh/PjxXLx4kTFjxuT63C1atMDJyYmnn36aAQMGkJyczLRp04iPj7eqGxUVxeLFi5k2bRq1a9e2ymBf75133mHZsmU0bdqUoUOH4uvryxdffMEPP/zAuHHj8PLyynVfb2Xx4sU4ODjQokUL9uzZw9tvv0316tWtxrB7e3vTuXNnpk2bRkhICI8++ugdnbdx48a0bt2aWbNm8eabbxIWFsaIESMYMmQIhw8fplWrVvj4+HDmzBm2bNmCm5sbw4cPx87OjuHDh9OjRw+efPJJunXrxsWLFxk+fDhBQUG3HeZxt+7vI488wuzZs6lUqRLVqlVj27ZtjB8/Ps9fluXj40P//v0ZOXIkL7zwAk899RQnTpxg2LBhOR6KExUVxdq1a/n+++8JCgrCw8PD4lOXnj17Mm7cOLZt28ann35603Zu9zMTGhqao+dSRIqAQp68KyJiXhXn2ubk5GTy9/c3NW7c2DR69GhTXFxctsctXbrUVK9ePZOzs7PJzc3N1KxZM9Nvv/1mUefayh9nz57N9pxHjhwxl33//fem6tWrm5ydnU2lSpUyvfHGG6affvrJBJjWrFljrnfhwgXTk08+afL29jYZDAbT9b9KuWHVFpPJZNq1a5fp0UcfNXl5eZmcnJxM1atXN82aNcuizrWVTL7++muL8iNHjpgAq/o3unad27ZtMz366KMmd3d3k4eHh+npp582nTlzJttj1q5dawJMY8aMuWXb17u2Kk52du3aZbKzszM999xz5rKlS5eamjZtavL09DQZjUZTSEiI6cknnzStWrXK4tjp06ebypcvb3JycjJVqFDB9Nlnn5natm1rqlmzpkW9wrq/8fHxpueff97k7+9vcnV1Nd13332mX3/91dS4cWOLFWxyc57MzExTdHS0qUyZMiYnJydTtWrVTN9//71VmzezY8cOU8OGDU2urq43XUmnSZMmJl9fX9PVq1et9uX2Zyanz6WIFB6DyXTd59giIvKf0a9fP6ZNm8aJEyesJnsWtosXL1KhQgUee+wxpk+fXtjdsUlxcXGEhITQq1evbNf0HzZsGMOHD+fs2bP5PtdDRAqHhuKIiPzH/P777xw4cICPPvqIHj16FHpQHxsby6hRo2jatCl+fn4cO3aMSZMmkZiYyOuvv16ofbNFJ0+e5PDhw4wfPx47OzvdQ5H/EAX2IiL/MdcmFz/yyCPmya6FyWg0cvToUXr27MmFCxfMk14//vhjqlSpUtjdszmffvopI0aMIDQ0lC+++MJixRsRKd40FEdEREREpBjQcpciIiIiIsWAAnsRERERkWJAgb2IiIiISDGgwF5EREREpBjQqjhSJHRcs76wuyB30Zg6lwq7C3IXlXIrU9hdkLvIM3RsYXdB7qKk418W2rldyj5dYG0X5nXdCWXsRURERESKAWXsRURERMTmGAzKT99Igb2IiIiI2ByDBp5Y0R0RERERESkGlLEXEREREZujoTjWdEdERERERIoBZexFRERExOYoY29Nd0REREREpBhQxl5EREREbI7BYCjsLhQ5ytiLiIiIiBQDytiLiIiIiA1SfvpGCuxFRERExOZo8qw13RERERERkWJAGXsRERERsTnK2FvTHRERERERKQaUsRcRERERm2NQftqK7oiIiIiISDGgjL2IiIiI2ByNsbemOyIiIiIiUgwoYy8iIiIiNkcZe2sK7EVERETE5iiwt6Y7IiIiIiJSDChjLyIiIiI2x4ChsLtQ5ChjLyIiIiJSDChjLyIiIiI2R2PsremOiIiIiIgUA8rYi4iIiIjNUcbemu6IiIiIiEgxoIy9iIiIiNgcZeytKbAXERERERukwP5GuiMiIiIiIsWAMvYiIiIiYnM0FMea7oiIiIiISDGgjL2IiIiI2Bxl7K3pjoiIiIiIFAPK2IuIiIiIzTEoP21Fd0REREREpBhQxl5EREREbI7G2FtTYC8iIiIiNsdgMBR2F4ocvdUpRKGhoUyePLnItXW9rl278thjj+V7uyIiIiKSv4pFxj42NpZRo0bxww8/cOrUKfz9/alRowa9e/emWbNm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b1HG/r9FGfv/lsLM2D+0ouAy9j89mPOMfVGSp4z99OnTzWu3r1tnuZqJwWBQYC8iIiIiBUozFazlKbA/cuRIfvdDRERERETuQJ7Xsb/m2kie3KyxKSIiIiJyJ4rKqjhFSZ4/xfj888+JiorCxcUFFxcXqlWrxty5c/OzbyIiIiIikkN5ythPnDiRt99+m1dffZWGDRtiMpn47bffeOmllzh37twtvw1VREREROROFZVVcYqSPAX277//vtXX5LZt25YqVaowbNgwBfYiIiIiUqA0edZanu5JTExMtl9v26BBA2JiYu64UyIiIiIikjt5CuzLly/PwoULrcoXLFhARETEHXdKRERERORW7AwFt9mqPA3FGT58OB06dGD9+vU0bNgQg8HAhg0bWL16dbYBv4iIiIiIFKw8BfZPPPEEmzdvZtKkSSxduhSTyURkZCRbtmyhZs2a+d1HERERERELBi13aSXP69jXrl2befPm5WdfREREREQkj3Ic2CckJODp6Wn+/61cqyciIiIiUhBseSx8QclxYO/j40NMTAz+/v54e3tn+02zJpMJg8FARkZGvnZSRERERERuLceB/S+//IKvry8Aa9asKbAOiYiIiIjcjtaxt5bjwL5x48bZ/l9ERERE5G6z0+RZK3maPLtz585syw0GA87OzpQtWxaj0XhHHRMRERERkZzLU2Bfo0aNbMfYX+Po6EiHDh345JNPcHZ2znPnRERERESyo8mz1vI0PGnJkiVEREQwffp0duzYwfbt25k+fToVK1Zk/vz5zJw5k19++YW33norv/srIiIiIiLZyFPGftSoUUyZMoWWLVuay6pVq0bp0qV5++232bJlC25ubvTr14/33nsv3zorIiIiIgKaPJudPN2TXbt2ERISYlUeEhLCrl27gKzhOjExMXfWOxERERERyZE8BfaVKlVizJgxpKammsvS0tIYM2YMlSpVAuDUqVMEBATkTy9FRERERK5jZyi4zVblaSjOhx9+SJs2bShdujTVqlXDYDCwc+dOMjIyWLZsGQCHDx+mZ8+e+dpZERERERHJXp4C+wYNGnD06FHmzZvHgQMHMJlMPPnkkzzzzDN4eHgA8L///S9fOyoiIiIico3WsbeWp8AewN3dnZdeeik/+yIiIiIikiO2PGSmoOR5QvHcuXO57777CA4O5tixYwBMmjSJb7/9Nt86JyIiIiIiOZOnwH7atGn07duXhx56iPj4eDIyMgDw8fFh8uTJ+dk/ERERERErdgW42ao89f39999nxowZDBkyBAeHf0fz1KlTx7zcpYiIiIiI3D15GmN/5MgRatasaVVuNBq5cuXKHXdKRERERORWNHnWWp4y9mFhYezYscOq/KeffqJy5cp32icREREREcmlPGXs33jjDV555RWSk5MxmUxs2bKFL7/8ktGjRzNz5sz87qOIiIiIiAWtimMtT4H9c889R3p6OgMGDODq1as888wzlCpVivfff59GjRrldx9FREREROQ28jzxt3v37hw7doy4uDhiY2PZsmUL27dvp3z58vnZPxERERERK3aGgttsVa4C+4sXL9KpUydKlixJcHAwU6dOxdfXlw8//JDy5cvz+++/89lnnxVUX0VEREREAC13mZ1cDcUZPHgw69evp0uXLixfvpw+ffqwfPlykpOT+fHHH2ncuHFB9VNERERERG4hV4H9Dz/8wKxZs2jevDk9e/akfPnyVKhQQV9KJSIiIiJ3lZa7tJarTxtOnz5NZGQkAOHh4Tg7O/PCCy8USMdERERERCTncpWxz8zMxNHR0fzY3t4eNze3fO+UiIiIiMit2PIk14KSq8DeZDLRtWtXjEYjAMnJybz00ktWwf3ixYvzr4ciIiIiInJbuQrsu3TpYvH42WefzdfOiIiIiIjkhC2vXlNQchXYz5o1q6D6If9x9gbH21eSYmN+y4uF3QW5i7afz9N3IYqN+vC5vYXdBbmbtjQp7B7IdfTbVkRERERsjsbYW1NgLyIiIiI2x6DlLq1oeJKIiIiISDGgjL2IiIiI2BwNxbGmjL2IiIiISDGgjL2IiIiI2Bxlp63pnoiIiIiIFAPK2IuIiIiIzbHTqjhWlLEXERERESkGlLEXEREREZujVXGsKbAXEREREZujwN6ahuKIiIiIiBQDytiLiIiIiM2xL+wOFEHK2IuIiIiIFAPK2IuIiIiIzdFyl9aUsRcRERERKQaUsRcRERERm6NVcawpYy8iIiIiUgwoYy8iIiIiNkcZe2sK7EVERETE5tgrsLeioTgiIiIiIsWAMvYiIiIiYnM0FMeaMvYiIiIiIsWAMvYiIiIiYnP0BVXWlLEXERERESkGlLEXEREREZujMfbWlLEXERERESkGlLEXEREREZtjX9gdKIKU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x80lKfEq3v4+NO/yMHUfbgiAvaM9h3ccYNO360hNSsGrpA8V7omkaadW2On5LlLefe9XXu9xD+8MuB8/Hxfizl3hqyV7+PDTP8x1HmgUyth3mpkfTx79IADvz9jK+zO2kpaWSf26pejcsRpuLo7EnLnM2t+O8cGnW8m8xac4InllMP3XIi8pki6n/VLYXZC7KObq1cLugtxF288XqRySFLC3Oh4u7C7IXXRgS89CO/f3x38qsLYfLftQgbVdkJQeEBEREREpBpRGERERERGbozH21pSxFxEREREpBpSxFxERERGbY6+MvRVl7EVEREREigFl7EVERETE5tjpC6qsKLAXEREREZujYSfWdE9ERERERIoBZexFRERExOZouUtrytiLiIiIiBQDytiLiIiIiM3RcpfWlLEXERERESkGlLEXEREREZuj5S6tKWMvIiIiIlIMKGMvIiIiIjZHq+JYU2AvIiIiIjZHgb01DcURERERESkGlLEXEREREZuj7LQ13RMRERERkWJAGXsRERERsTkGjbG3ooy9iIiIiEgxoIy9iIiIiNgcJeytKWMvIiIiIlIMKGMvIiIiIjZHY+ytKbAXEREREZujYSfWdE9ERERERIoBZexFRERExOYYDKbC7kKRo4y9iIiIiEgxoIy9iIiIiNgczZ21poy9iIiIiEgxoIy9iIiIiNgcLXdpTRl7EREREZFiQBl7EREREbE5SthbU2AvIiIiIjbHTpG9FQ3FEREREREpBpSxFxERERGbo4S9NWXsRURERESKAWXsRURERMTmaLlLa8rYi4iIiIgUA8rYi4iIiIjNUcLemgJ7KRIG/6GX53+Jg51rYXdB7qKJ9UoXdhfkLloQ7VbYXRD5z1JgLyIiIiI2RylBawrsRURERMTm6AuqrGnyrIiIiIhIMaCMvYiIiIjYHCXsrSljLyIiIiJSDChjLyIiIiI2x2AwFXYXihxl7EVEREREigFl7EVERETE5miMvTVl7EVEREREigFl7EVERETE5hiUsreijL2IiIiISDGgjL2IiIiI2Bxlp60psBcRERERm6OhONb0ZkdEREREpBhQxl5EREREbI4S9taUsRcRERERKQYU2IuIiIiIzTEYCm67E9HR0RgMBnr37m0uM5lMDBs2jODgYFxcXGjSpAl79uyxOC4lJYVevXpRokQJ3NzcaNOmDSdP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"/>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=e8fa80d7-fa74-4f7c-bfe8-d4fc61dc3716">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># ניתן להסיק כי בתל אביב ובמחוז המרכז נעשה שימוש מצומצם בכרטיס אשראי וכדאי לפעול להגדיל אותו</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=02e46eca-7320-467a-96cc-dfb23bcb887a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [31]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># הצגת תדירות הפעמים עבור כל סכום תרומה</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">6</span><span class="p">))</span>
<span class="n">counts</span><span class="p">,</span> <span class="n">bins</span><span class="p">,</span> <span class="n">patches</span><span class="o">=</span><span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">donations_with_regions</span><span class="p">[</span><span class="s2">"Amount"</span><span class="p">],</span> <span class="n">bins</span><span class="o">=</span><span class="mi">15</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s1">'skyblue'</span><span class="p">,</span> <span class="n">edgecolor</span><span class="o">=</span><span class="s1">'black'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">"Donation Amounts"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">"Amount"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">"Frequency"</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">axis</span><span class="o">=</span><span class="s1">'y'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'--'</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.7</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">bins</span><span class="o">.</span><span class="n">round</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span> 
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[31]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>([&lt;matplotlib.axis.XTick at 0x1b3c0686850&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0c80cd0&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0c81450&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0c81bd0&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0c82350&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0c82ad0&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0c83250&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0c839d0&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d48190&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d48910&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d49090&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d49810&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d49f90&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d4a710&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d4ae90&gt;,
  &lt;matplotlib.axis.XTick at 0x1b3c0d4b610&gt;],
 [Text(100.0, 0, '100'),
  Text(115.0, 0, '115'),
  Text(131.0, 0, '131'),
  Text(146.0, 0, '146'),
  Text(161.0, 0, '161'),
  Text(177.0, 0, '177'),
  Text(192.0, 0, '192'),
  Text(207.0, 0, '207'),
  Text(223.0, 0, '223'),
  Text(238.0, 0, '238'),
  Text(253.0, 0, '253'),
  Text(269.0, 0, '269'),
  Text(284.0, 0, '284'),
  Text(299.0, 0, '299'),
  Text(315.0, 0, '315'),
  Text(330.0, 0, '330')])</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAqYAAAIhCAYAAACcznj/AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAXHJJREFUeJzt3Xl4VOX9/vH7zCQTQiQJZAFCkAgIQYGggoqI4gKIuNtWcRdqcUetadW2X6S1QqF1qVqKLUatFdyA+jMFi8qigEokAfFiJ4JAEBJCAgEySeb5/RFyyCSZbEwyR3m/riut85knZz7Pc86cuXNmEixjjBEAAAAQYq5QNwAAAABIBFMAAAA4BMEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMALe7VV1+VZVn2V5s2bdSpUydddNFFmjx5svbs2RPqFv28+eabeu655+q8z7IsPfnkk63aT01//etfZVmW+vbtG9I+Wkp96w/gx83inyQF0NJeffVV3XnnncrIyFBqaqrKysq0Z88effbZZ8rIyJDb7dZbb72lSy+9NNStSpKuuOIKrV27Vt9++22t+z7//HMlJycrOTm59Rs7asCAAVq9erXdzznnnBOyXlpCfesP4MeNK6YAWk3fvn117rnnaujQobr++uv17LPPas2aNYqKitJ1112n77//PtQtNujcc88NaSjNysrS6tWrNXr0aEnSzJkzQ9YLAAQbwRRASJ188sn6y1/+ogMHDmjGjBl+973//vsaPHiw2rZtq3bt2mn48OFasWKF35gnn3xSlmXpm2++0ZgxYxQTE6OOHTtq7NixKioq8hv70ksv6YILLlBiYqKioqLUr18/TZ06VWVlZfaYYcOGKTMzU9u2bfP7+EGVut7KX7t2ra6++mq1b99ebdq00YABA/Taa6/5jVm8eLEsy9KsWbP0m9/8RklJSYqOjtall16qDRs2NHq9qoLolClTdN5552n27Nk6dOiQ35hvv/1WlmVp2rRp+tOf/qSUlBRFRkZq2LBh2rhxo8rKyvTYY48pKSlJMTExuvbaa2t9nMLn82nq1KlKTU1VRESEEhMTddttt2nHjh1+41JSUnTHHXfU6nPYsGEaNmxYk+ff0PpPnz5daWlpOumkk9SuXTulpqbqiSeeaPT6AXA2gimAkLv88svldru1dOlSu/bmm2/q6quvVnR0tGbNmqWZM2eqsLBQw4YN02effVZrG9dff7169eql9957T4899pjefPNNPfzww35jtmzZoptuukn/+te/9MEHH2jcuHGaNm2axo8fb4/529/+piFDhqhTp05asWKF/RXIhg0bdN555+mbb77RX//6V82ZM0ennXaa7rjjDk2dOrXW+CeeeELbtm3TP//5T7388svatGmTrrzySlVUVDS4TocPH9asWbM0aNAg9e3bV2PHjtWBAwf0zjvv1Dn+pZde0rJly/TSSy/pn//8p9avX68rr7xS48aN0969e/XKK69o6tSp+uijj/Tzn//c73vvuece/frXv9bw4cP1/vvv6w9/+IMWLFig8847T/n5+Q32GkhD869v/WfPnq17771XF154oebOnat58+bp4YcfVklJSbP7AeAwBgBaWEZGhpFkVq5cGXBMx44dTZ8+fYwxxlRUVJikpCTTr18/U1FRYY85cOCASUxMNOedd55dmzhxopFkpk6d6re9e++917Rp08b4fL46H6+iosKUlZWZ119/3bjdbrNv3z77vtGjR5tu3brV+X2SzMSJE+3bN954o4mIiDDbt2/3Gzdq1CjTtm1bs3//fmOMMYsWLTKSzOWXX+437u233zaSzIoVKwKszDGvv/66kWT+/ve/G2Mq1+Okk04yQ4cO9RuXm5trJJm0tDS/9XvuueeMJHPVVVf5jX/ooYeMJFNUVGSMMWbdunVGkrn33nv9xn3xxRdGknniiSfsWrdu3cztt99eq9cLL7zQXHjhhfbtpsw/0Prff//9JjY2to6VAfBjwRVTAI5gqv0e5oYNG7Rr1y7deuutcrmOnaZOOukkXX/99fr8889rvX191VVX+d3u37+/jhw54vcWdXZ2tq666irFxcXJ7XYrPDxct912myoqKrRx48Zm9f3JJ5/okksuUdeuXf3qd9xxhw4dOlTramtdfUrStm3bGnysmTNnKjIyUjfeeKOkyvX46U9/qk8//VSbNm2qNf7yyy/3W78+ffpIkv351Jr17du3S5IWLVpkz6G6s88+W3369NHHH3/cYK+BHM/8zz77bO3fv19jxozRf/7zn+O6cgvAmQimAEKupKREBQUFSkpKkiQVFBRIkjp37lxrbFJSknw+nwoLC/3qcXFxfrcjIiIkVb79LVWGrqFDh2rnzp16/vnn9emnn2rlypV66aWX/MY1VUFBQcA+q8+lsX0GsnnzZi1dulSjR4+WMUb79+/X/v379ZOf/ESS9Morr9T6ng4dOvjd9ng89daPHDni13OgedWcU1M0d/6SdOutt+qVV17Rtm3bdP311ysxMVHnnHOOFi5c2Ox+ADgLwRRAyGVmZqqiosL+ZZmq8JKXl1dr7K5du+RyudS+ffsmPca8efNUUlKiOXPm6JZbbtH555+vgQMH2qGsueLi4gL2KUnx8fHHtf0qr7zyiowxevfdd9W+fXv7q+rq52uvvdaoz6k2RkPrX31Obdq0UWlpaa1xLXU1884779Ty5ctVVFSkzMxMGWN0xRVXNOqKKwDnI5gCCKnt27fr0UcfVUxMjP1LSL1791aXLl305ptv+r3FX1JSovfee8/+Tf2mqPrN7qordFLlxwf+8Y9/1BobERHR6Cuol1xyiT755BM7iFZ5/fXX1bZtW5177rlN6rMuFRUVeu2119SjRw8tWrSo1tcvf/lL5eXlaf78+cf9WJJ08cUXS5LeeOMNv/rKlSu1bt06XXLJJXYtJSVFa9as8Ru3cePGJv2lgZoas/5RUVEaNWqUfvOb38jr9eqbb75p9uMBcI6wUDcA4MSxdu1alZeXq7y8XHv27NGnn35q/4H9uXPnKiEhQZLkcrk0depU3Xzzzbriiis0fvx4lZaWatq0adq/f7+mTJnS5McePny4PB6PxowZo1/96lc6cuSIpk+fXusjAZLUr18/zZkzR9OnT9dZZ50ll8ulgQMH1rndiRMn6oMPPtBFF12k//u//1OHDh3073//W5mZmZo6dapiYmKa3GtN8+fP165du/SnP/3J708wVenbt69efPFFzZw5U1dcccVxP17v3r31i1/8Qi+88IJcLpdGjRqlb7/9Vr/73e/UtWtXv792cOutt+qWW27Rvffeq+uvv17btm3T1KlT7X3ZHIHW/6677lJkZKSGDBmizp07a/fu3Zo8ebJiYmI0aNCg4543gNAjmAJoNXfeeaekys80xsbGqk+fPvr1r3+tn//857WCzE033aSoqChNnjxZN9xwg9xut84991wtWrRI5513XpMfOzU1Ve+9955++9vf6rrrrlNcXJxuuukmPfLIIxo1apTf2AkTJuibb77RE088oaKiIhlj/K7cVte7d28tX75cTzzxhO677z4dPnxYffr0UUZGRp1/37M5Zs6cKY/HY69fTfHx8br22mv17rvvBu0fKZg+fbp69OihmTNn6qWXXlJMTIwuu+wyTZ482e9zojfddJN27dqlv//978rIyFDfvn01ffp0TZo0qdmPHWj9hw4dqldffVVvv/22CgsLFR8fr/PPP1+vv/76cQVhAM7BP0kKAAAAR+AzpgAAAHAEgikAAAAcgWAKAAAARyCYAgAAwBEIpgAAAHAEgikAAAAc4Qf9d0x9Pp927dqldu3a2f+qCwAAAJzDGKMDBw4oKSlJLlf910R/0MF0165d6tq1a6jbAAAAQAO+++47JScn1zvmBx1M27VrJ6lyotHR0SHuBgAAADUVFxera9eudm6rzw86mFa9fR8dHU0wBQAAcLDGfOySX34CAACAIxBMAQAA4AgEUwAAADgCwRQAAACOQDAFAACAIxBMAQAA4AgEUwAAADgCwRQAAACOQDAFAACAIxBMAQAA4AgEUwAAADgCwRQAAACOQDAFAACAIxBMAQAA4AgEUwAAADhCSINpSkqKLMuq9XXfffeFsi0AAACEQFgoH3zlypWqqKiwb69du1bDhw/XT3/60xB2BQAAgFAIaTBNSEjwuz1lyhT16NFDF154YYg6AgAAQKiENJhW5/V69cYbb+iRRx6RZVl1jiktLVVpaal9u7i4WJJUXl6u8vJySZLL5ZLL5ZLP55PP57PHVtUrKipkjGmw7na7ZVmWvd3qdUl+V3rrq4eFhckY41e3LEtut7tWj4HqzIk5hWpOO3bs0L59+2SM8eux6mM3Ta1X33ZVXZLf2PrqLpdLxhjFxcUpOTm5WXNqqf20Y8cO5efnN3tOwVjfuuoJCQnq0qXLD+7Y+zE+n5gTczpR51RzfH0cE0znzZun/fv364477gg4ZvLkyZo0aVKtenZ2tqKioiRVXoXt0aOHcnNztXfvXntMcnKykpOTtXHjRhUVFdn17t27KzExUWvXrtXhw4ftempqqmJjY5Wdne230P3795fH41FWVpZfDwMHDpTX69WaNWvsmtvt1qBBg1RUVKT169fb9cjISKWlpSk/P19bt2616zExMerTp4927dqlHTt22HXmxJxCMafDhw/rry+8oHlz52r06NEaMGCAPf7TTz/V0qVLNWbMGHXv3t2uZ2ZmKicnR+PHj1d8fLxdnzVrlrZu3ar09HR5PB67PmPGDBUXFys9Pd1vTtOmTVN0dLTGjx9v17xer6ZNm6bu3bvr5ltu0UXDhikyMtIR++ngwYNatHixfBUVzZ7TmDFj7Hp+fr5mzJihAQMGaPTo0XZ969atmjVrli644AINHTrUrufk5CgzM7PO/bQyK0uLPvnE78XF6cdeS+0n5sScmFNo5pSdna3GskzNH99DZOTIkfJ4PPp//+//BRxT1xXTrl27qqCgQNHR0ZJC/1PBj/EnHeZ0Ys4pJydHgwcP1nVPvqCOp/RU9fcxjCQjSy75nz4C1Su3GKhe+7cwA9ct7c3dpLm/n6Bly5ZpwIABjthPOTk5GjJkiK6f+LziUno2eU6SqbNuyajm+0d11avWvWb9+9zNeuu39ygrK0tpaWlNmlN1PJ+YE3NiTsczp8LCQsXFxamoqMjOa4E44orptm3b9NFHH2nOnDn1jouIiFBEREStelhYmMLC/KdStag1VS1SY+s1t9ucumVZddYD9djUOnNiToHqxzMnl8ul8vJyJZ5yqpL6pNUaG0per1cul8tvbqHcTy6XS16vV3Epp6qLg9bKdzSmBjoOnHrsNab+Q3s+NabOnJhToPqPcU6BOOLvmGZkZCgxMdHvLSsAAACcWEIeTH0+nzIyMnT77bc3KVEDAADgxyXkwfSjjz7S9u3bNXbs2FC3AgAAgBAK+SXKESNG1PrzKQAAADjxhPyKKQAAACARTAEAAOAQBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjkAwBQAAgCMQTAEAAOAIBFMAAAA4AsEUAAAAjhDyYLpz507dcsstiouLU9u2bTVgwAB99dVXoW4LAAAArSwslA9eWFioIUOG6KKLLtL8+fOVmJioLVu2KDY2NpRtAQAAIARCGkz/9Kc/qWvXrsrIyLBrKSkpoWsIAAAAIRPSYPr+++9r5MiR+ulPf6olS5aoS5cuuvfee3XXXXfVOb60tFSlpaX27eLiYklSeXm5ysvLJUkul0sul0s+n08+n88eW1WvqKiQMabButvtlmVZ9nar1yWpoqKiUfWwsDAZY/zqlmXJ7XbX6jFQnTkxp1DMyefzKSzs6CnC+GRV69FYlmS5ZBmf5Fd3SZYVuO7z79FYlZ8msoyvcXWXW5KRx+ORz+dTeXm5I/aTz+eTx+ORS8aed5PmZIx/3bIqxwes170/atYtVf63McbveHL6sVe9xx/L84k5MacTeU41x9cnpMF069atmj59uh555BE98cQT+vLLL/Xggw8qIiJCt912W63xkydP1qRJk2rVs7OzFRUVJUlKSEhQjx49lJubq71799pjkpOTlZycrI0bN6qoqMiud+/eXYmJiVq7dq0OHz5s11NTUxUbG6vs7Gy/he7fv788Ho+ysrL8ehg4cKC8Xq/WrFlj19xutwYNGqSioiKtX7/erkdGRiotLU35+fnaunWrXY+JiVGfPn20a9cu7dixw64zJ+YUijkVFRVp5MiRkqT2B3cr6vB+e3xxVIKKoxIUV/Sd2nhL7Hphu84qiWyvjoW5Cis/9kNkfuzJOuI5SUn7NsmqdlLc3aGHKlxh6pK/wW9OO+N7y+0rV6d9W+yacbm0Mz5V7Vw+paenq6CgQFlZWY7YT/v27VN6erpSIo5of4W3yXNqU1ai+P3b7Xp5WIR2d+ihqCP71f5Anl0/4olSfmw3RR8qUHTJsd5LImNV2C6p1n4qc1e+GBQXF/sdN04/9qQf3/OJOTGnE3lO2dnZaizLVI/Crczj8WjgwIFavny5XXvwwQe1cuVKrVixotb4uq6Ydu3aVQUFBYqOjpYU+p8Kfow/6TCnE3NOOTk5Gjx4sO5+bYG6pPZzzBXTnety9PKdo7Vs2TINGDDAEfspJydHQ4YM0d0ZmeqcmtbkObXUFdOdG77WCzcPV1ZWltLS0po0p+p4PjEn5sScjmdOhYWFiouLU1FRkZ3XAgnpFdPOnTvrtNNO86v16dNH7733Xp3jIyIiFBERUaseFhZ27C3Ho6oWtaaqRWpsveZ2m1O3LKvOeqAem1pnTswpUP145uRyuY6dfCyXjFX7MSsDZxPqrrrnaqym1C15vV65XC6/uYVyP7lcLnm9XvlkSZZVT+8B6pbVxHrd+6Nm3RzdCYGOA6cee42p/9CeT42pMyfmFKj+Y5xTICH9c1FDhgzRhg3+b3dt3LhR3bp1C1FHAAAACJWQBtOHH35Yn3/+uZ5++mlt3rxZb775pl5++WXdd999oWwLAAAAIRDSYDpo0CDNnTtXs2bNUt++ffWHP/xBzz33nG6++eZQtgUAAIAQCOlnTCXpiiuu0BVXXBHqNgAAABBiIf8nSQEAAACJYAoAAACHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcISQBtMnn3xSlmX5fXXq1CmULQEAACBEwkLdwOmnn66PPvrIvu12u0PYDQAAAEIl5ME0LCys0VdJS0tLVVpaat8uLi6WJJWXl6u8vFyS5HK55HK55PP55PP57LFV9YqKChljGqy73W5ZlmVvt3pdkioqKhpVDwsLkzHGr25Zltxud60eA9WZE3MKxZx8Pp/Cwo6eIoxPVrUejWVJlkuW8Ul+dZdkWYHrPv8ejVX5po1lfI2ru9ySjDwej3w+n8rLyx2xn3w+nzwej1wy9rybNCdj/OuWVTk+YL3u/VGzbqnyv40xfseT04+96j3+WJ5PzIk5nchzqjm+PiEPpps2bVJSUpIiIiJ0zjnn6Omnn1b37t3rHDt58mRNmjSpVj07O1tRUVGSpISEBPXo0UO5ubnau3ev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8hMAAACapVnBtC6nnnqqpkyZUutqKgAAANAYQQumkuR2u7Vr165gbhIAAAAniGZ9xvT999/3u22MUV5enl588UUNGTIkKI0BAADgxNKsYHrNNdf43bYsSwkJCbr44ov1l7/8JRh9AQAA4ATTrGDq8/mC3QcAAABOcEH9jCkAAADQXM26YvrII480euwzzzzTnIcAAADACaZZwTQ7O1urVq1SeXm5evfuLUnauHGj3G63zjzzTHucZVnB6RIAAAA/es0KpldeeaXatWun1157Te3bt5dU+Uf377zzTg0dOlS//OUvg9okAAAAfvya9RnTv/zlL5o8ebIdSiWpffv2euqpp/itfAAAADRLs4JpcXGxvv/++1r1PXv26MCBA8fdFAAAAE48zQqm1157re688069++672rFjh3bs2KF3331X48aN03XXXRfsHgEAAHACaNZnTP/+97/r0Ucf1S233KKysrLKDYWFady4cZo2bVpQGwQAAMCJoVnBtG3btvrb3/6madOmacuWLTLGqGfPnoqKigp2fwAAADhBHNcf2M/Ly1NeXp569eqlqKgoGWOC1RcAAABOMM0KpgUFBbrkkkvUq1cvXX755crLy5Mk/fznP+dPRQEAAKBZmhVMH374YYWHh2v79u1q27atXb/hhhu0YMGCoDUHAACAE0ezPmP6v//9Tx9++KGSk5P96qeeeqq2bdsWlMYAAABwYmnWFdOSkhK/K6VV8vPzFRERcdxNAQAA4MTTrGB6wQUX6PXXX7dvW5Yln8+nadOm6aKLLgpacwAAADhxNOut/GnTpmnYsGHKysqS1+vVr371K33zzTfat2+fli1bFuweAQAAcAJo1hXT0047TWvWrNHZZ5+t4cOHq6SkRNddd52ys7PVo0ePYPcIAACAE0CTr5iWlZVpxIgRmjFjhiZNmtQSPQEAAOAE1OQrpuHh4Vq7dq0sy2qJfgAAAHCCatZb+bfddptmzpwZ7F4AAABwAmvWLz95vV7985//1MKFCzVw4EBFRUX53f/MM88EpTkAAACcOJoUTLdu3aqUlBStXbtWZ555piRp48aNfmN4ix8AAADN0aRgeuqppyovL0+LFi2SVPlPkP71r39Vx44dW6Q5AAAAnDia9BlTY4zf7fnz56ukpCSoDQEAAODE1KxffqpSM6gCAAAAzdWkYGpZVq3PkPKZUgAA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/vvvdeuttyovL08xMTHq37+/FixYoOHDh4eyLQAAAIRASIPpzJkzQ/nwAAAAcBDHfcYUAAAAJyaCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEQimAAAAcASCKQAAAByBYAoAAABHIJgCAADAEUIaTCdPnqxBgwapXbt2SkxM1DXXXKMNGzaEsiUAAACESEiD6ZIlS3Tffffp888/18KFC1VeXq4RI0aopKQklG0BAAAgBMJC+eALFizwu52RkaHExER99dVXuuCCC0LUFQAAAEIhpMG0pqKiIklShw4d6ry/tLRUpaWl9u3i4mJJUnl5ucrLyyVJLpdLLpdLPp9PPp/PHltVr6iokDGmwbrb7ZZlWfZ2q9clqaKiolH1sLAwGWP86pZlye121+oxUL2hORlj5PF45JKR5auQsVySZckyPqnanOy6z79HY1VeOLeMr3F1l1syxr9uWZXjj9bdluyeKr/JJ8uvF0uyXAHrAXs/zjlVtmrZa9WUOdWuB29OfutlTKvtp/rm5LYqj9/KjbXufqpvTpbkd7y35n4KNKda+6+Jc2qpY886+v+1jvcQnyOqr5dlfK22n+rrvaonHd2Hrbmf6p2TpPDwcPl8Pvv16If0+tSar7nHHt//eA/pOUKVx9W6devs/iyr8plZff711ate56vXLcuSZVnHVY+Pj9fJJ5/cKvup5vj6OCaYGmP0yCOP6Pzzz1ffvn3rHDN58mRNmjSpVj07O1tRUVGSpISEBPXo0UO5ubnau3evPSY5OVnJycnauHGjHYAlqXv37kpMTNTatWt1+PBhu56a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GY0bN04///nP1adPHz333HPq2rWrpk+fHsq2AAAAEAJhoXpgr9err776So899phffcSIEVq+fHmd31NaWqrS0lL7dlFRkSRp3759Ki8vlyS5XC65XC75fD75fD57bFW9oqJCxpgG6263W5Zl2duVpOLiYknSznVrVHbooF9vVd9p1ejZyLL/t2bdklFNzanv275Z4eHh2r3+WF91jTdHO6y7XlfvzZ/Tvu1bFB4errz1a+Q9VBK0uR7vnPZ+u0mS/NaqsXNqyXrVeu1ev0beQwebNKeWOvb2bd8it9td5/HelO0c6zE4c8r/dlOjjveWrlefU+3913r7qb56wbbNkqS89XWds0J3jqi+XmWHDrbafqqv96qedq6r3IehOJfXVd/77SaFhYXVON4bN6eG682bU0vsv2DMad/2LZKkXXW+RofmHLG3zvNV4+dUte1gH3sF27cqPDxcBw4cUHFx8XFlo6q6JFVUVNRZLywsrOzB1O6rdqMhsnPnTiPJLFu2zK/+xz/+0fTq1avO75k4caJR5b7jiy+++OKLL7744usH9PXdd981mA9DdsW0imX5/wxgjKlVq/L444/rkUcesW/7fD7t27dPcXFxAb8nmIqLi9W1a1d99913io6ObvHHawwn9lTFib3RU9M4sTd6ahon9ua0npzWT3VO7I2emsaJvbV2T8YYHThwQElJSQ2ODVkwjY+Pl9vt1u7du/3qe/bsUceOHev8noiICEVERPjVYmNjW6rFgKKjox1zcFVxYk9VnNgbPTWNE3ujp6ZxYm9O68lp/VTnxN7oqWmc2Ftr9hQTE9OocSH75SePx6OzzjpLCxcu9KsvXLhQ5513Xoi6AgAAQKiE9K38Rx55RLfeeqsGDhyowYMH6+WXX9b27dt19913h7ItAAAAhEBIg+kNN9yggoIC/f73v1deXp769u2r//73v+rWrVso2wooIiJCEydOrPVxglByYk9VnNgbPTWNE3ujp6ZxYm9O68lp/VTnxN7oqWmc2JsTe6piGdOY390HAAAAWlbI/0lSAAAAQCKYAgAAwCEIpgAAAHAEgikAAAAcgWAqaenSpbryyiuVlJQky7I0b948v/uNMXryySeVlJSkyMhIDRs2TN98843fmNLSUj3wwAOKj49XVFSUrrrqKu3YsaNF+pkzZ45Gjhyp+Ph4WZalnJycWtsYNmyYLMvy+7rxxhub1U9T+3vyySeVmpqqqKgotW/fXpdeeqm++OILvzEvv/yyhg0bpujoaFmWpf3797dYP9WNHz9elmXpueeeq3XfihUrdPHFFysqKkqxsbEaNmyYDh8+3GI9rVu3TldddZViYmLUrl07nXvuudq+fbt9fzDXqCm91Txuqr6mTZsmSfr2228DjnnnnXdapKfvv/9ed9xxh5KSktS2bVtddtll2rRpk33/vn379MADD6h3795q27atTj75ZD344IMqKipqVj+TJ0/WoEGD1K5dOyUmJuqaa67Rhg0b/MY0dF5oiXVqTG9lZWX69a9/rX79+ikqKkpJSUm67bbbtGvXLr/tjB8/Xj169FBkZKQSEhJ09dVXa/369S3Sk9S488Lu3bt16623qlOnToqKitKZZ56pd999t8V6uuOOO2rtm3PPPddvTDDXqSm9SQ2fI7Zs2aJrr71WCQkJio6O1s9+9jN9//33LdbTwYMHdf/99ys5OVmRkZHq06ePpk+fXuf2jDEaNWpUg+fk4+2poXODFNx1qjJ9+nT179/f/gP1gwcP1vz58+37Q/E63VBPjXkOBjPLNBfBVFJJSYnS0tL04osv1nn/1KlT9cwzz+jFF1/UypUr1alTJw0fPlwHDhywxzz00EOaO3euZs+erc8++0wHDx7UFVdcoYqKiqD3U1JSoiFDhmjKlCn1bueuu+5SXl6e/TVjxowm99Kc/nr16qUXX3xRX3/9tT777DOlpKRoxIgR2rt3rz3m0KFDuuyyy/TEE0+0eD9V5s2bpy+++KLOfxJtxYoVuuyyyzRixAh9+eWXWrlype6//365XM17ijTU05YtW3T++ecrNTVVixcv1urVq/W73/1Obdq0sccEc42a0lv1YyYvL0+vvPKKLMvS9ddfL0nq2rVrrTGTJk1SVFSURo0aFfSejDG65pprtHXrVv3nP/9Rdna2unXrpksvvVQlJSWSpF27dmnXrl3685//rK+//lqvvvqqFixYoHHjxjWrnyVLlui+++7T559/roULF6q8vFwjRoywH09q+LzQEuvUmN4OHTqkVatW6Xe/+51WrVqlOXPmaOPGjbrqqqv8tnPWWWcpIyND69at04cffihjjEaMGNGsc1Zj1qsx54Vbb71VGzZs0Pvvv6+vv/5a1113nW644QZlZ2e3SE+SdNlll/nto//+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2rRpplevXub99983q1evNi+88II56aST7LfE//Of/5iePXuaAwcO2N8TrGAaqKfGnBtaap1KS0vNpk2bzMqVK81jjz1m4uPjzTfffOM3prVfpxvqqb7nYEtmmaYgmNZQ80m0ZcsWI8msWrXKb9xVV11lbrvtNmOMMR9//LGRZPbt2+c3pn///ub//u//gtpPdU054H0+X63PjgRDY086PXv2NE8//XSteksH02effdY+GVV9STIul8t069bNGGPM1q1bjSTzr3/9y29bP/vZz8xNN90U9J5KS0tNWFiY+cMf/uA37le/+pU577zzan1/qILp0qVLjSSTk5MT8Ptff/11Ex4ebvbs2dMqPe3fv99+rLPPPtvce++9fvcXFxebwYMHm0suuSQoweH+++83ycnJZuvWrX71xpwXqmuJdQrUWxWv12uuueYa079/f5Ofn9/g9kpLS03btm3Nm2++2WI91VT9vLB58+Zanxc0xphLLrnkuF4Um9NT9c8O1xSMdWqot6aeI/bu3WufHzp27GimTp0a9J4OHTpkwsPDzQcffOBXHzdunP3D2IQJEwKeby+88MKg91RdQ+cGY4K7TnW55JJLal1ZDPXrdF09VVf9OdiSWaYp+IxpA0455RR16tRJCxcutGter1dLlizReeedJ6nytzbDw8P9xuTl5Wnt2rX2mFD75ptvVFZWps6dO4fk8Y0x9ueBWtOtt96qNWvWKCcnx/5KSkpSenq6PvzwQ0lSSkqKkpKSav0Zko0bN6pbt25B78nj8WjQoEGt9njNNXPmTJ111ln1fjZ45syZuuqqq5SQkNAqPcXExCghIUGbNm1SVlaWrr76avu+4uJijRgxQh6PR++//77f586ayhij+++/X3PmzNEnn3yiU045xe/+xpwXqgvmOjXUm1T5J6N+9rOfadOmTfroo48UFxfX6G0353namJ4aerxDhw5JUq2/hOF2u5v129PN6amgoEDfffddg+fJ4z2fNdRbU88R8fHxio2N1SeffKI9e/bU+gsMweiprKxMZWVl9e6fxx57rNb5VpKeffZZZWRkBL2n6uo7N1QJxjo11O/xHBct8TrdUE/V73dMlmm1COxgBw4cMNnZ2SY7O9tIsj/TU/UbrFOmTDExMTFmzpw55uuvvzZjxowxnTt3NsXFxfY27r77bpOcnGw++ugjs2rVKnPxxRebtLQ0U15eHvR+CgoKTHZ2tsnMzDSSzOzZs012drbJy8szxlReeZg0aZJZuXKlyc3NNZmZmSY1NdWcccYZzeqnKf0dPHjQPP7442bFihXm22+/NV999ZUZN26ciYiI8LsSkpeXZ7Kzs80//vEPI8ksXbrUZGdnm4KCgqCvV011/Vb+s88+a6Kjo80777xjNm3aZH7729+aNm3aNPuzZA31NGfOHBMeHm5efvlls2nTJvPCCy8Yt9ttPv30U3sbwVyjpvRmTOXb4W3btjXTp08PuJ1NmzYZy7LM/Pnzj6ufxvT09ttvm0WLFpktW7aYefPmmW7dupnrrrvO/v7i4mJzzjnnmH79+pnNmzebvLw8+6s5x/w999xjYmJizOLFi/22dejQIXtMY84LxgR3nRrTW1lZmbnqqqtMcnKyycnJ8RtTWlpqjKm84vv000+brKwss23bNrN8+XJz9dVXmw4dOtT5kZvj7akx5wWv12t69uxphg4dar744guzefNm8+c//9lYllXnZ/eOt6cDBw6YX/7yl2b58uUmNzfXLFq0yAwePNh06dLF3ofBXqfG9mZM484Rr7zyilmxYoXZvHmz+de//mU6dOhgHnnkkRbr6cILLzSnn366WbRokdm6davJyMgwbdq0MX/7298CblfH8VZ+Y3pq6NxgTHDXqcrjjz9uli5danJzc82aNWvME088YVwul/2Z6FC8TtfXU2Nfm4OZZZqLYGqOvVVa8+v22283xlReXp84caLp1KmTiYiIMBdccIH5+uuv/bZx+PBhc//995sOHTqYyMhIc8UVV5jt27e3SD8ZGRl13j9x4kRjjDHbt283F1xwgenQoYPxeDymR48e5sEHHzzuQNOY/g4fPmyuvfZak5SUZDwej+ncubO56qqrav2Sw8SJE+vcRkZGRlD7qUtdwdQYYyZPnmySk5NN27ZtzeDBg/1eAFqip5kzZ5qePXuaNm3amLS0NDNv3jy/bQRzjZra24wZM0xkZKTZv39/wO08/vjjJjk52VRUVBxXP43p6fnnnzfJyckmPDzcnHzyyea3v/2tHbLq+35JJjc3t8n9BNpW9bVvzHnBmOCuU2N6q3rrsK6vRYsWGWMqP8M4atQok5iYaMLDw01ycrK56aabzPr161ukp8aeFzZu3Giuu+46k5iYaNq2bWv69+9f65drgtXToUOHzIgRI0xCQoJ9XN1+++1+5+1gr1Nje6vS0Dni17/+tenYsaMJDw83p556qvnLX/5i/5JnS/SUl5dn7rjjDpOUlGTatGljevfu3eBjHk8wbUxPDZ0bjAnuOlUZO3as6datm/F4PCYhIcFccsklfr+oF4rX6fp6auxzMJhZprksY4wRAAAAEGJ8xhQAAACOQDAFAACAIxBMAQAA4AgEUwAAADgCwRQAAACOQDAFAACAIxBMAQAA4AgEUwAAADgCwRQAAACOQDAFgCZavny53G63LrvsslC30iTDhg3TQw89FOo2ACAggikANNErr7yiBx54QJ999pm2b98e6nYA4EeDYAoATVBSUqK3335b99xzj6644gq9+uqr9n2LFy+WZVn68MMPdcYZZygyMlIXX3yx9uzZo/nz56tPnz6Kjo7WmDFjdOjQIfv7SktL9eCDDyoxMVFt2rTR+eefr5UrV9r3v/rqq4qNjfXrY968ebIsy7795JNPasCAAfrXv/6llJQUxcTE6MYbb9SBAwckSXfccYeWLFmi559/XpZlybIsffvtty2yRgDQXARTAGiCt956S71791bv3r11yy23KCMjQ8YYvzFPPvmkXnzxRS1fvlzfffedfvazn+m5557Tm2++qczMTC1cuFAvvPCCPf5Xv/qV3nvvPb322mtatWqVevbsqZEjR2rfvn1N6m3Lli2aN2+ePvjgA33wwQdasmSJpkyZIkl6/vnnNXjwYN11113Ky8tTXl6eunbtevwLAgBBRDAFgCaYOXOmbrnlFknSZZddpoMHD+rjjz/2G/PUU09pyJAhOuOMMzRu3DgtWbJE06dP1xlnnKGhQ4fqJz/5iRYtWiSp8grs9OnTNW3aNI0aNUqnnXaa/vGPfygyMlIzZ85sUm8+n0+vvvqq+vbtq6FDh+rWW2+1e4uJiZHH41Hbtm3VqVMnderUSW63OwgrAgDBQzAFgEbasGGDvvzyS914442SpLCwMN1www165ZVX/Mb179/f/u+OHTuqbdu26t69u19tz549kiqvcpaVlWnIkCH2/eHh4Tr77LO1bt26JvWXkpKidu3a2bc7d+5sPw4A/BCEhboBAPihmDlzpsrLy9WlSxe7ZoxReHi4CgsL7Vp4eLj935Zl+d2uqvl8Pvv7q2rVGWPsmsvlqvVxgbKyslr91fc4APBDwBVTAGiE8vJyvf766/rLX/6inJwc+2v16tXq1q2b/v3vfzdruz179pTH49Fnn31m18rKypSVlaU+ffpIkhISEnTgwAGVlJTYY3Jycpr8WB6PRxUVFc3qEwBaA1dMAaARPvjgAxUWFmrcuHGKiYnxu+8nP/mJZs6cqWeffbbJ242KitI999yj9PR0dejQQSeffLKmTp2qQ4cOady4cZKkc845R23bttUTTzyhBx54QF9++aXfXwNorJSUFH3xxRf69ttvddJJJ6lDhw5yubg+AcA5OCMBQCPMnDlTl156aa1QKknXX3+9cnJytGrVqmZte8qUKbr++ut166236swzz9TmzZv14Ycfqn379pKkDh066I033tB///tf9evXT7NmzdKTTz7Z5Md59NFH5Xa7ddpppykhIYG/wQrAcSxT84NLAAAAQAhwxRQAAACOQDAFAACAIxBMAQAA4AgEUwAAADgCwRQAAACOQDAFAACAIxBMAQAA4AgEUwAAADgCwRQAAACOQDAFAACAIxBMAQAA4Aj/HzCwaewMYU9AAAAAAElFTkSuQmCC"/>
</div>
</div>
</div>
</div>
</div>
</main>
</body>
</html>
