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

            sdwebui_sharedopts = JSON.parse(shopts.innerText)

            if (sdwebui_sharedopts) {
                const quicksettings = gradioApp().getElementById("quicksettings")
                const txt2img_settings = gradioApp().getElementById("txt2img_settings")

                if (getopt("artuitw_quicksettings2settings", false)) {
                    txt2img_settings.insertBefore(quicksettings, txt2img_settings.firstElementChild)
                }

                if (getopt("artuitw_settings2promptswidth", false)) {
                    const promptContainer = gradioApp().getElementById("txt2img_prompt_container")
                    promptContainer.appendChild(txt2img_settings)

                    txt2img_actions_column.appendChild(gradioApp().getElementById("txt2img_results"))
                    gradioApp().getElementById("txt2img_prompt_container").style.flexGrow = getopt("artuitw_settings2promptsXratio", 1)

                    gradioApp().getElementById("txt2img_tools").appendChild(
                        gradioApp().getElementById("txt2img_styles_row")
                    )
                }

                if (getopt("artuitw_min_generate", false)) {
                    const gen = gradioApp().getElementById("txt2img_generate_box")
                    const firstButton = gradioApp().querySelector("#txt2img_tools button")
                    firstButton.parentElement.insertBefore(gen, firstButton)

                    gradioApp().getElementById("txt2img_tools").style.alignContent = "flex-end"
                    gradioApp().getElementById("txt2img_styles_row").style.alignContent = "flex-end"

                }

            }
        }
        else {
            setTimeout(onload, 2000);
        }
    };
    onload();
});
