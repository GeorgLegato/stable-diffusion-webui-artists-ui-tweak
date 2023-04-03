from modules import script_callbacks, scripts, shared
import os
import gradio as gr

usefulDirs = scripts.basedir().split(os.sep)[-2:]

txt2img_gallery_component=None
quicksettings_component=None
txt2img_setting_component=None
generate_button = None

def after_component(component, **kwargs):
    global txt2img_gallery_component
    global quicksettings_component
    global txt2img_gallery_component

    
    if kwargs.get("elem_id") == "quicksettings":
            quicksettings_component = component



"""
            if (not component.parent.elem_id): return
            if (component.parent.elem_id == "image_buttons_txt2img" or component.parent.elem_id == "image_buttons_img2img" or component.parent.elem_id == "image_buttons_extras"):                    
                suffix = component.parent.elem_id
            else:
                return

            with gr.Accordion("Panorama", open=False, elem_id="PanoramaViewer_ToolBox", visible=True):
                    with gr.Row():
                        view_gallery_button = gr.Button ("\U0001F310", variant="tool", elem_id="sendto_panogallery_button_"+suffix)        # 🌐
                        view_cube_button    = gr.Button ("\U0001F9CA", variant="tool",elem_id="sendto_panogallery_cube_button_"+ suffix)   # 🧊
                        view_gallery_button.click (None, [],None, _js="panorama_here(\""+iframesrc_gal+"\",\"\",\""+view_gallery_button.elem_id+"\")" )
                        view_cube_button.click    (None, [],None, _js="panorama_here(\""+iframesrc_gal+"\",\"cubemap\",\""+view_cube_button.elem_id+"\")" )
                        
                        #╬═
                        conv_cubemap_gallery_button = gr.Button ("\U0000271C", variant="tool", elem_id="convertto_cubemap_button"+suffix)  #✜
                        conv_cubemap_gallery_button.click (None, [],None, _js="convertto_cubemap" )

                        close_panoviewer = gr.Button("\U0000274C", variant="tool") # ❌
                        close_panoviewer.click(None,[],None,_js="panorama_here(\"""\",\"\",\"""\")" )

                        gallery_input_ondrop = gr.Textbox(visible=False, elem_id="gallery_input_ondrop_"+ suffix)
                        gallery_input_ondrop.style(container=False)

            if (gallery_input_ondrop and txt2img_gallery_component):
                gallery_input_ondrop.change(fn=dropHandleGallery, inputs=[gallery_input_ondrop], outputs=[txt2img_gallery_component]) 


    if kwargs.get("elem_id") == "txt2img_gallery":
        txt2img_gallery_component = component
        if (gallery_input_ondrop and txt2img_gallery_component):
            gallery_input_ondrop.change(fn=dropHandleGallery, inputs=[gallery_input_ondrop], outputs=[txt2img_gallery_component]) s
"""

def add_tab():
    import json 
      
    json_object = json.dumps(shared.opts.data, indent = 4) 
#    print(json_object)

    with gr.Blocks(analytics_enabled=False) as ui:
#        with gr.Column():
#            upload_button = gr.UploadButton("Upload movie...", file_types=["video"], file_count="single")
#            upload_button.upload(fn=None, inputs=upload_button, outputs=None, _js="setPanoFromDroppedFile")
            V = gr.HTML(value="<script id='sdwebui_sharedopts_script'>"+json_object+"</script>", elem_id="art-ui-tw-sh-options")
    return [(V, "artists-ui-tweak", "artists-ui-tweak")]

def on_ui_settings():
    section = ('artists-ui-tweak', "Artists UI Tweak")

    shared.opts.add_option("artuitw_min_generate", shared.OptionInfo(
        True, "Minimize Generate button as tool icon", gr.Checkbox, {"interactive": True}, section=section))

    shared.opts.add_option("artuitw_prompt_sidebyside", shared.OptionInfo(
        True, "Split prompts to side-by-side ", gr.Checkbox, {"interactive": True}, section=section))

    shared.opts.add_option("artuitw_quicksettings2settings", shared.OptionInfo(
        True, "Move quicksettings to image setting panel ", gr.Checkbox, {"interactive": True}, section=section))

    shared.opts.add_option("artuitw_settings2promptswidth", shared.OptionInfo(
        True, "Bring prompts and setting into one column left side ", gr.Checkbox, {"interactive": True}, section=section))

    shared.opts.add_option("artuitw_settings2promptsXratio", shared.OptionInfo(
        1, "If setting2prompt width, which width-ratio between both columns (0: minimize setting, 1: 50/50,  6: minimize output gallery column)", gr.Slider, {"minimum": 0, "maximum": 6, "step": 0.1}, section=section))


"""
    shared.opts.add_option("control_net_model_config", shared.OptionInfo(
        default_conf, "Config file for Control Net models", section=section))
    shared.opts.add_option("control_net_model_adapter_config", shared.OptionInfo(
        default_conf_adapter, "Config file for Adapter models", section=section))
    shared.opts.add_option("control_net_detectedmap_dir", shared.OptionInfo(
        default_detectedmap_dir, "Directory for detected maps auto saving", section=section))
    shared.opts.add_option("control_net_models_path", shared.OptionInfo(
        "", "Extra path to scan for ControlNet models (e.g. training output directory)", section=section))
    shared.opts.add_option("control_net_max_models_num", shared.OptionInfo(
        1, "Multi ControlNet: Max models amount (requires restart)", gr.Slider, {"minimum": 1, "maximum": 10, "step": 1}, section=section))
    shared.opts.add_option("control_net_model_cache_size", shared.OptionInfo(
        1, "Model cache size (requires restart)", gr.Slider, {"minimum": 1, "maximum": 5, "step": 1}, section=section))
    shared.opts.add_option("control_net_control_transfer", shared.OptionInfo(
        False, "Apply transfer control when loading models", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_no_detectmap", shared.OptionInfo(
        False, "Do not append detectmap to output", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_detectmap_autosaving", shared.OptionInfo(
        False, "Allow detectmap auto saving", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_only_midctrl_hires", shared.OptionInfo(
        True, "Use mid-control on highres pass (second pass)", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_allow_script_control", shared.OptionInfo(
        False, "Allow other script to control this extension", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_skip_img2img_processing", shared.OptionInfo(
        False, "Skip img2img processing when using img2img initial image", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_monocular_depth_optim", shared.OptionInfo(
        False, "Enable optimized monocular depth estimation", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_only_mid_control", shared.OptionInfo(
        False, "Only use mid-control when inference", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("control_net_cfg_based_guidance", shared.OptionInfo(
        False, "Enable CFG-Based guidance", gr.Checkbox, {"interactive": True}, section=section))
    # shared.opts.add_option("control_net_advanced_weighting", shared.OptionInfo(
    #     False, "Enable advanced weight tuning", gr.Checkbox, {"interactive": False}, section=section))
"""

script_callbacks.on_ui_tabs(add_tab)
script_callbacks.on_after_component(after_component)
script_callbacks.on_ui_settings(on_ui_settings)