/*
 @licstart  The following is the entire license notice for the JavaScript code in this file.

 The MIT License (MIT)

 Copyright (C) 1997-2020 by Dimitri van Heesch

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software
 and associated documentation files (the "Software"), to deal in the Software without restriction,
 including without limitation the rights to use, copy, modify, merge, publish, distribute,
 sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or
 substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 @licend  The above is the entire license notice for the JavaScript code in this file
*/
var NAVTREE =
[
  [ "Open-CMSIS-Pack", "index.html", [
    [ "Overview", "index.html", "index" ],
    [ "Technical background", "cp_Packs.html", [
      [ "Software Components", "cp_Packs.html#cp_Components", [
        [ "Component classification", "cp_Packs.html#cp_CompDetails", null ],
        [ "Software Component Files", "cp_Packs.html#cp_CompFiles", null ],
        [ "File naming", "cp_Packs.html#cp_CompFileNaming", null ]
      ] ],
      [ "References", "cp_Packs.html#cp_Cond", null ],
      [ "Requirements", "cp_Packs.html#cp_Requirements", null ],
      [ "Central API definition", "cp_Packs.html#cp_APIDef", null ],
      [ "Inventory header file", "cp_Packs.html#cp_RTECompH", null ],
      [ "Combining components", "cp_Packs.html#cp_Combine", null ],
      [ "Pack Conventions", "cp_Packs.html#PackFilenames", [
        [ "Pack File Name", "cp_Packs.html#pack_filename", null ],
        [ "Software Component Cclasses", "cp_Packs.html#pack_Cclass", null ]
      ] ]
    ] ],
    [ "Pack tutorials", "cp_PackTutorial.html", null ],
    [ "Publish a CMSIS-Pack", "createPackPublish.html", [
      [ "Checking CMSIS-Packs", "createPackPublish.html#createPackUtil", null ],
      [ "Local installation", "createPackPublish.html#cp_LocalInstallation", null ],
      [ "Web download", "createPackPublish.html#cp_WebDownload", [
        [ "Self-hosted packs", "createPackPublish.html#cp_HowWebDownloadWorks", null ],
        [ "GitHub-hosted packs", "createPackPublish.html#cp_GitHubHosting", [
          [ "PIDX file on GitHub", "createPackPublish.html#gh_pidx", null ],
          [ "PDSC file on GitHub", "createPackPublish.html#gh_pdsc", null ]
        ] ]
      ] ],
      [ "Using a pack index service", "createPackPublish.html#cp_KeilComPack", [
        [ "The vidx2pidx conversion tool", "createPackPublish.html#cp_vidx2pidx", null ],
        [ "Rehosting a pack", "createPackPublish.html#cp_PackRehosting", null ],
        [ "Renaming a pack", "createPackPublish.html#cp_PackRenaming", null ]
      ] ],
      [ "Pack index files", "createPackPublish.html#packIndexFile", [
        [ "Package index file (PIDX)", "createPackPublish.html#pidxFile", null ],
        [ "Vendor index file (VIDX)", "createPackPublish.html#vidxFile", null ],
        [ "Index schema file", "createPackPublish.html#packIndexSchema", null ]
      ] ]
    ] ],
    [ "Pack Description (*.pdsc) Format", "packFormat.html", "packFormat" ],
    [ "Configuration Wizard Annotations", "configWizard.html", [
      [ "Annotation Rules", "configWizard.html#configWizard_annotations", null ],
      [ "Code Example", "configWizard.html#configWizard_codeExample", null ],
      [ "Tool-specific display", "configWizard.html#configWizard_display", null ]
    ] ],
    [ "Flash Programming", "flashAlgorithm.html", "flashAlgorithm" ],
    [ "Debug Setup with CMSIS-Pack", "coresight_setup.html", "coresight_setup" ],
    [ "System Description File (*.SDF) Format", "sdf_pg.html", [
      [ "SDF top level structure", "sdf_pg.html#sdf_structure", null ],
      [ "/system_description", "sdf_pg.html#sdf_element_system_description", null ],
      [ "/system_description/debug_and_trace_config", "sdf_pg.html#sdf_element_debug_and_trace_config", null ],
      [ "/system_description/debug_and_trace_config/debug", "sdf_pg.html#sdf_element_debug", null ],
      [ "/system_description/.../config_item", "sdf_pg.html#sdf_element_config_item", [
        [ "Debug element", "sdf_pg.html#autotoc_md3", null ],
        [ "Device element", "sdf_pg.html#autotoc_md4", null ],
        [ "Trace element", "sdf_pg.html#autotoc_md5", null ]
      ] ],
      [ "/system_description/debug_and_trace_config/trace", "sdf_pg.html#sdf_element_trace", null ],
      [ "/system_description/debug_and_trace_config/trace/trace_capture", "sdf_pg.html#sdf_element_trace_capture", null ],
      [ "/system_description/platform", "sdf_pg.html#sdf_element_platform", null ],
      [ "/system_description/platform/scanchain", "sdf_pg.html#sdf_element_scanchain", null ],
      [ "/system_description/platform/scanchain/dap", "sdf_pg.html#sdf_element_dap", null ],
      [ "/system_description/platform/scanchain/device", "sdf_pg.html#sdf_element_device", null ],
      [ "/system_description/platform/scanchain/../../config_items", "sdf_pg.html#sdf_element_config_items", null ],
      [ "/system_description/platform/scanchain/../../device_info_items", "sdf_pg.html#sdf_element_device_info_items", null ],
      [ "/system_description/platform/scanchain/../../device_info_items/device_info_item", "sdf_pg.html#sdf_element_device_info_item", null ],
      [ "/system_description/platform/topology", "sdf_pg.html#sdf_element_topology", null ],
      [ "/system_description/platform/topology/topology_link", "sdf_pg.html#sdf_element_topology_link", null ],
      [ "/system_description/platform/clusters", "sdf_pg.html#sdf_element_clusters", null ],
      [ "/system_description/platform/clusters/cluster", "sdf_pg.html#sdf_element_cluster", null ]
    ] ]
  ] ]
];

var NAVTREEINDEX =
[
"algorithmFunc.html",
"sdf_pg.html#sdf_element_cluster"
];

var SYNCONMSG = 'click to disable panel synchronisation';
var SYNCOFFMSG = 'click to enable panel synchronisation';