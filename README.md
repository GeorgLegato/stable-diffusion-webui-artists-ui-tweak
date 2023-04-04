# stable-diffusion-webui-artists-ui-tweak
A great, small extension to reorganise UI-Elements of SD-Webui to have a clean layout and focus on the ouput image.
Space was saved to enlarge gallery and have a axial, modular layout.

* Currently in this beta the gui modifications are limited on the txt2img-tab
* Ignore in my screenshot the dark theme, it is applied using my browser-setting. This extension does not do any colors.
* Pre-requisite: This extension is dedicated to the current SD-Webui with Gradio3.23-update as of March 2023.

# Example screenshots
## Only styles active, no other tweaks.
This example show right column width is twice of the left one.  
It keeps large prompt area, if you are a prompt focussed.
![image](https://user-images.githubusercontent.com/7210708/229652155-92a69dfd-75b0-4712-8d08-2a8cb77da3f4.png)

## Move Quicksettings down to normal settings panel
This brings the Tab-button to the upper row, where they actually belong to.
![image](https://user-images.githubusercontent.com/7210708/229652468-a0551ae8-5e61-42cb-aafe-407ea2caaeee.png)
![image](https://user-images.githubusercontent.com/7210708/229652866-0e3bf37b-c0c4-4475-a6da-2cb9b6574ba6.png)


## Combine prompts and technical sliders to one left column
Smaller prompts, so even more space for the output gallery. But the generate button is too large and wastes space...
![image](https://user-images.githubusercontent.com/7210708/229653133-5416254e-4ed3-4c94-9fff-ad5280b43290.png)
![image](https://user-images.githubusercontent.com/7210708/229653412-dc1d235a-3f4f-440c-b629-e4036fe7791b.png)


## Save space on generate button, all in a single row
Bring Generate Button, Tools and the Style dropdown in one row and align it at bottom line.
Todo: Generate button as high as tools.

![image](https://user-images.githubusercontent.com/7210708/229653677-07e10017-3439-4ed7-8221-3d13efbcf61a.png)
![image](https://user-images.githubusercontent.com/7210708/229653833-5264aa3b-9b1e-412d-9f53-f5289b5901cd.png)

## All settings on, 8 images in gallery
![image](https://user-images.githubusercontent.com/7210708/229654057-5f707b6a-7a17-4c64-8092-0a532eb271b4.png)

## Thats why we need this:
Large preview on single selected image from the gallery.
![image](https://user-images.githubusercontent.com/7210708/229654119-e03091d3-abfa-4906-9397-13810b288f5c.png)


# Installation
1) Open your SD-Webui
2) Goto Extension Tab
3) add Extenion by pasting this URL, since this extension is not public in the repository, yet
https://github.com/GeorgLegato/stable-diffusion-webui-artists-ui-tweak



## Settings

### Style.css
* Per default all settings are false or inactive.  
* This extension ships a style.css which provides the basic idea: make the left column with sliders and extension panels less dominant.  
That room will be used by the gallery to win widht and height. The height can be tweak (mannually in beta) here:
![image](https://user-images.githubusercontent.com/7210708/229649321-c6af6c19-ed9c-431c-9f9b-e71b5d18be84.png)
It is located in this extension-folder in ```style.css```. 
* ```Flex:2``` means the column with output gallery is twice as width as the technical left column, enter number here like 0.5 or 1.5 or 3.5 whatever.
* ```Height: 80vh``` means the output gallery panel will always take 80% of your available screen size (viewport height). Don´t forget you have button above and a footer. Find your height.

### Extension-Setting-Tab
![image](https://user-images.githubusercontent.com/7210708/229650150-6d6a0f73-acb0-4d19-b613-19d3b80b6ce4.png)
This extension provides an own settings category ```Artists UI Tweak```

** After changing any setting ```Restart I``` **



