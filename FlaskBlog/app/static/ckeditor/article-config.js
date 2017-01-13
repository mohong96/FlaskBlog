/**
 * Created by Administrator on 2017/1/10 0010.
 */
CKEDITOR.editorConfig = function( config ) {
            config.toolbar= [
                { name: 'clipboard', items: [ 'Undo', 'Redo' ] },
                { name: 'styles', items: [ 'Styles', 'Format' ] },
                { name: 'basicstyles', items: [ 'Bold', 'Italic', 'Strike', '-', 'RemoveFormat' ] },
                { name: 'paragraph', items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote' ] },
                { name: 'links', items: [ 'Link', 'Unlink' ] },
                { name: 'insert', items: [ 'Image', 'EmbedSemantic', 'Table' ] },
                { name: 'tools', items: [ 'Maximize' ] },
                { name: 'editing', items: [ 'Scayt' ] }
            ];
            config.stylesSet= [
                /* Inline Styles */
                { name: 'Marker',			element: 'span', attributes: { 'class': 'marker' } },
                { name: 'Cited Work',		element: 'cite' },
                { name: 'Inline Quotation',	element: 'q' },
                /* Object Styles */
                {
                    name: 'Special Container',
                    element: 'div',
                    styles: {
                        padding: '5px 10px',
                        background: '#eee',
                        border: '1px solid #ccc'
                    }
                },
                {
                    name: 'Compact table',
                    element: 'table',
                    attributes: {
                        cellpadding: '5',
                        cellspacing: '0',
                        border: '1',
                        bordercolor: '#ccc'
                    },
                    styles: {
                        'border-collapse': 'collapse'
                    }
                },
                { name: 'Borderless Table',		element: 'table',	styles: { 'border-style': 'hidden', 'background-color': '#E6E6FA' } },
                { name: 'Square Bulleted List',	element: 'ul',		styles: { 'list-style-type': 'square' } },
                /* Widget Styles */
                // We use this one to style the brownie picture.
                { name: 'Illustration', type: 'widget', widget: 'image', attributes: { 'class': 'image-illustration' } },
                // Media embed
                { name: '240p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-240p' } },
                { name: '360p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-360p' } },
                { name: '480p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-480p' } },
                { name: '720p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-720p' } },
                { name: '1080p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-1080p' } }
            ];
            // Enabling extra plugins, available in the standard-all preset: http://ckeditor.com/presets-all
            config.customConfig='';
            config.extraPlugins= 'autoembed,embedsemantic,uploadimage,image2,uploadfile';
            /*********************** File management support ***********************/
            // In order to turn on support for file uploads, CKEditor has to be configured to use some server side
            // solution with file upload/management capabilities, like for example CKFinder.
            // For more information see http://docs.ckeditor.com/#!/guide/dev_ckfinder_integration
            // Uncomment and correct these lines after you setup your local CKFinder instance.
            // filebrowserBrowseUrl: 'http://example.com/ckfinder/ckfinder.html',
            // filebrowserUploadUrl: 'http://example.com/ckfinder/core/connector/php/connector.php?command=QuickUpload&type=Files',
            /*********************** File management support ***********************/
            // Remove the default image plugin because image2, which offers captions for images, was enabled above.
            config.removePlugins='image';
            // Make the editing area bigger than default.
            config.height= 461;
            // An array of stylesheets to style the WYSIWYG area.
            // Note: it is recommended to keep your own styles in a separate file in order to make future updates painless.
            config.contentsCss= [ 'https://cdn.ckeditor.com/4.6.1/standard-all/contents.css', '../static/ckeditor/article-style.css' ];
            // This is optional, but will let us define multiple different styles for multiple editors using the same CSS file.
            config.bodyClass= 'article-editor';
            // Reduce the list of block elements listed in the Format dropdown to the most commonly used.
            config.format_tags= 'p;h1;h2;h3;pre';
            // Simplify the Image and Link dialog windows. The "Advanced" tab is not needed in most cases.
            config.removeDialogTabs= 'image:advanced;link:advanced';
            // Define the list of styles which should be available in the Styles dropdown list.
            // If the "class" attribute is used to style an element, make sure to define the style for the class in "mystyles.css"
            // (and on your website so that it rendered in the same way).
            // Note: by default CKEditor looks for styles.js file. Defining stylesSet inline (as below) stops CKEditor from loading
            // that file, which means one HTTP request less (and a faster startup).
            // For more information see http://docs.ckeditor.com/#!/guide/dev_styles

            //图片上传至路由地址
            config.filebrowserImageUploadUrl = '/imageUpload'

};