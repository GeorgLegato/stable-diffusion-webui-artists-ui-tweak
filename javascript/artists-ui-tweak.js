let txt2img_settings = null
let quicksettings = null
let sdwebui_sharedopts = null


function getopt(optnanme, defaultValue = true) {
    if (sdwebui_sharedopts[optnanme] === undefined) return defaultValue
    else return sdwebui_sharedopts[optnanme]
}


document.addEventListener("DOMContentLoaded", () => {
    const onload = () => {

        if (typeof gradioApp === "function") {

            shopts = gradioApp().querySelector("#sdwebui_sharedopts_script")
            if (!shopts) {
                setTimeout(onload, 2000);
                return
            }

            txt2img_settings = gradioApp().getElementById("txt2img_settings")
            if (!txt2img_settings) {
                setTimeout(onload, 2000);
                return
            }
            quicksettings = gradioApp().getElementById("quicksettings")
            if (!quicksettings) {
                setTimeout(onload, 2000);
                return
            }

            /* hide our pseudo-tab */
            const tabbuttons = gradioApp().querySelectorAll(".tab-nav>button")
            tabbuttons.forEach((b) => { if ("artists-ui-tweak" == b.innerText) b.style.display = "none" })

            sdwebui_sharedopts = JSON.parse(shopts.innerText)

            if (sdwebui_sharedopts) {

                if (getopt("artuitw_quicksettings2settings", false)) {
                    const txt2img_settings = gradioApp().getElementById("txt2img_settings")
                    const quicksettings = gradioApp().getElementById("quicksettings")
                    txt2img_settings.insertBefore(quicksettings, txt2img_settings.firstElementChild)
                }


                {
                    const galVH = getopt("artuitw_galleryheightVH", 50)
                    const txt2imgGalleryContainer = document.querySelector('#txt2img_gallery_container');
                    const img2imgGalleryContainer = document.querySelector('#img2img_gallery_container');
                  
                    if (txt2imgGalleryContainer) {
                        txt2imgGalleryContainer.style.height=galVH+"vh"
                    }
                    if (img2imgGalleryContainer) {
                        img2imgGalleryContainer.style.height=galVH+"vh"
                    }
                }

                if (getopt("artuitw_settings2promptswidth", false)) {
                    const txt2img_promp_container = gradioApp().getElementById("txt2img_prompt_container")
                    const exnet = gradioApp().querySelector("#txt2img_extra_networks.gradio-row").parentElement // + its form; attention tool-icon has same ID!
                    const txt2img_results = gradioApp().getElementById("txt2img_results")
                    const txt2img_tools = gradioApp().getElementById("txt2img_tools")
                    const txt2img_styles_row = gradioApp().getElementById("txt2img_styles_row")
                    const txt2img_generate_box = gradioApp().getElementById("txt2img_generate_box")
                    const txt2img_token_button = gradioApp().getElementById("txt2img_token_button")
                    const txt2img_negative_token_button = gradioApp().getElementById("txt2img_negative_token_button")
                    const txt2img_tool_icons = gradioApp().getElementById("txt2img_clear_prompt").parentElement // actual div has no id 

                    txt2img_promp_container.style.flexGrow = getopt("artuitw_settings2promptsXratio", 1)

                    /* align tool icon to the style bar */
                    txt2img_tool_icons.style.justifyContent="flex-end"


                    txt2img_promp_container.appendChild(txt2img_settings)

                    /* build up right column from scratch, so clean up action column first */
                    tmpdiv = document.createElement("div")
                    while (txt2img_actions_column.childNodes.length > 0) {
                        tmpdiv.appendChild(txt2img_actions_column.childNodes[0]);
                    }

                    if (txt2img_actions_column.children.length > 0) throw "should not happen"

                    {
                        txt2img_actions_column.appendChild(txt2img_tools)
                        txt2img_actions_column.appendChild(exnet)
                        txt2img_actions_column.appendChild(txt2img_results)
                        {
                            txt2img_tools.appendChild(txt2img_generate_box)
                            txt2img_tools.appendChild(txt2img_token_button)
                            txt2img_tools.appendChild(txt2img_negative_token_button)
                            txt2img_tools.appendChild(txt2img_tool_icons)
                            txt2img_tools.appendChild(txt2img_styles_row)
                            txt2img_tools.style.alignContent = "flex-end"
                            txt2img_styles_row.style.alignContent = "flex-end"
                        }
                    }
                }
            }
        }

        else {
            setTimeout(onload, 2000);
        }
    };
    onload();
});
