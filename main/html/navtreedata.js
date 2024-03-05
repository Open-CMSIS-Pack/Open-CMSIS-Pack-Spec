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
    [ "Software Pack Use Cases", "index.html#SWPackVariants", [
      [ "CMSIS-Pack in ARM::CMSIS Pack", "index.html#autotoc_md0", null ]
    ] ],
    [ "Revision History of CMSIS-Pack", "pack_revisionHistory.html", null ],
    [ "Overview", "cp_Packs.html", [
      [ "Software Components", "cp_Packs.html#cp_Components", [
        [ "Technical Details", "cp_Packs.html#cp_CompDetails", null ],
        [ "Software Component Files", "cp_Packs.html#cp_CompFiles", null ],
        [ "File naming", "cp_Packs.html#cp_CompFileNaming", null ]
      ] ],
      [ "References to other software components", "cp_Packs.html#cp_Cond", null ],
      [ "Requirements", "cp_Packs.html#cp_Requirements", null ],
      [ "Central API definition", "cp_Packs.html#cp_APIDef", null ],
      [ "Inventory header file: RTE_Components.h", "cp_Packs.html#cp_RTECompH", null ],
      [ "Combining software components", "cp_Packs.html#cp_Combine", null ],
      [ "Pack Conventions", "cp_Packs.html#PackFilenames", [
        [ "Pack File Name", "cp_Packs.html#pack_filename", null ],
        [ "Software Component Cclasses", "cp_Packs.html#pack_Cclass", null ]
      ] ]
    ] ],
    [ "Pack Tutorials", "cp_PackTutorial.html", [
      [ "Steps to Create a Pack", "cp_PackTutorial.html#cp_PackSteps", null ],
      [ "Pack with Software Components", "cp_PackTutorial.html#cp_SWComponents", [
        [ "Create PDSC File", "cp_PackTutorial.html#cp_CreatePDSC", null ],
        [ "Generate a Pack", "cp_PackTutorial.html#cp_GeneratePack", null ],
        [ "Software Components", "cp_PackTutorial.html#cp_TutorialComponents", null ],
        [ "Software Component Files", "cp_PackTutorial.html#autotoc_md1", null ],
        [ "Conditions", "cp_PackTutorial.html#cp_Conditions", null ],
        [ "Variants", "cp_PackTutorial.html#cp_Variants", null ],
        [ "RTE_Components.h", "cp_PackTutorial.html#cp_RTEComponents_h", null ],
        [ "Bundles", "cp_PackTutorial.html#cp_Bundles", null ],
        [ "Instances", "cp_PackTutorial.html#cp_Instances", null ],
        [ "API Interface", "cp_PackTutorial.html#cp_API", null ],
        [ "User Code Templates", "cp_PackTutorial.html#cp_CodeTemplates", null ],
        [ "Example Projects", "cp_PackTutorial.html#cp_Examples", null ]
      ] ],
      [ "Pack with Device Support", "cp_PackTutorial.html#createPack_DFP", [
        [ "DFP Use Cases", "cp_PackTutorial.html#autotoc_md2", null ],
        [ "Steps to Create a DFP", "cp_PackTutorial.html#autotoc_md3", null ],
        [ "Basic Device Family Pack", "cp_PackTutorial.html#cp_BasicDFP", null ],
        [ "System and Startup Files", "cp_PackTutorial.html#cp_System_Startup", null ],
        [ "System View Description File", "cp_PackTutorial.html#cp_SVD", null ],
        [ "Flash Programming Algorithms", "cp_PackTutorial.html#cp_FlashProgrammingAlgorithm", null ],
        [ "Debug Descriptions", "cp_PackTutorial.html#cp_debugdescription", null ],
        [ "Device Properties", "cp_PackTutorial.html#cp_DeviceProperties", null ],
        [ "Device Specific Software Components", "cp_PackTutorial.html#cp_DeviceSWComp", null ]
      ] ],
      [ "Pack with Board Support", "cp_PackTutorial.html#createPackBoard", [
        [ "BSP Use Cases", "cp_PackTutorial.html#autotoc_md4", null ],
        [ "Specify a Development Board", "cp_PackTutorial.html#cp_SpecDevBoard", null ],
        [ "Create a BSP Bundle", "cp_PackTutorial.html#cp_BundleExample", null ],
        [ "Add CMSIS-Drivers VIO", "cp_PackTutorial.html#cp_BSPVIO", null ],
        [ "Add Example Projects", "cp_PackTutorial.html#cp_BSPExamples", [
          [ "Platform example", "cp_PackTutorial.html#cp_BSPExPlatform", null ],
          [ "Blinky example", "cp_PackTutorial.html#cp_BSPExBlinky", null ]
        ] ]
      ] ]
    ] ],
    [ "Utilities for Creating Packs", "createPackUtil.html", "createPackUtil" ],
    [ "Publish a Pack", "createPackPublish.html", [
      [ "Prerequisites", "createPackPublish.html#cp_prerequisites", null ],
      [ "Local Installation", "createPackPublish.html#cp_LocalInstallation", null ],
      [ "Web Download", "createPackPublish.html#cp_WebDownload", null ],
      [ "Publish with Pack Index Service", "createPackPublish.html#cp_KeilComPack", null ],
      [ "Rehost pack to different URL", "createPackPublish.html#cp_PackRehosting", null ],
      [ "Rename a pack", "createPackPublish.html#cp_PackRenaming", null ],
      [ "Web Infra-structure", "createPackPublish.html#cp_HowWebDownloadWorks", null ]
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
        [ "Debug element", "sdf_pg.html#autotoc_md8", null ],
        [ "Device element", "sdf_pg.html#autotoc_md9", null ],
        [ "Trace element", "sdf_pg.html#autotoc_md10", null ]
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
    ] ],
    [ "Pack Index Files", "packIndexFile.html", [
      [ "Package Index File (pidx)", "packIndexFile.html#pidxFile", null ],
      [ "Vendor Index File (vidx)", "packIndexFile.html#vidxFile", null ],
      [ "CMSIS-Pack Index Schema File", "packIndexFile.html#packIndexSchema", null ]
    ] ]
  ] ]
];

var NAVTREEINDEX =
[
"algorithmFunc.html",
"pdsc_family_pg.html#element_trace_tracebuffer"
];

var SYNCONMSG = 'click to disable panel synchronisation';
var SYNCOFFMSG = 'click to enable panel synchronisation';