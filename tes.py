website_id = "generated-website-id"
# Creating the website with basic information
create_website_response = pyxl_ai__jit_plugin.CreateWebsiteOrUpdateWebsiteSettings({
    "websiteTitle": "Data Transformation",
    "orderColorSchema": "solid",
    "header": {
        "title": "Data Transformation"
    },
    "footer": {
        "description": "Hasil cantik dan mudah dioperasikan"
    },
    "colors": {
        "mainColor": "dark_orange",
        "secondColor": "orange"
    }
})

website_id = create_website_response['id']
# Adding Hero Block
add_hero_block_response = pyxl_ai__jit_plugin.AddHeroBlock({
    "hero": {
        "title": "Strategi bikin kerjaan lebih ringan dan analisa data lebih mudah",
        "subtitle": "Ubah data kamu jadi dashboard interaktif dan transformasi data otomatis",
        "button1": "Mau Dong!",
        "button1Link": "#services",
        "imagePrompt": "A professional working on a data dashboard"
    },
    "pageUrl": "/",
    "websiteId": website_id
})
# Adding About Section
add_features_block_response = pyxl_ai__jit_plugin.AddFeaturesBlock({
    "features": {
        "title": "About Me",
        "points": [
            {
                "title": "",
                "description": "Bisa cepat paham performa bisnis, cepat ambil keputusan berdasarkan data, dan kerjaan cepat selesai, pastinya bikin waktumu lebih lega dan ngga sibuk ngurus data secara manual yang bikin pusing + waktu banyak terbuang"
            },
            {
                "title": "3 Strategi Biar Kerjaan Cepat Kelar dan Analisa Data Lebih Mudah!",
                "description": ""
            }
        ]
    },
    "pageUrl": "/",
    "websiteId": website_id
})
# Adding Services Section
add_services_block_response = pyxl_ai__jit_plugin.AddFeaturesBlock({
    "features": {
        "title": "My Services",
        "points": [
            {
                "title": "Bikin Dashboard Interaktif",
                "description": "Dashboard ini penting banget biar kamu lebih cepat paham kondisi bisnis dan ambil kesimpulan berdasarkan data, dashboard yang efektif adalah dashboard yang interaktif, mudah dioperasikan, auto update, dan tampilan yang fresh, serta mampu meng-cover objektif dari user.",
                "imagePrompt": "Interactive Dashboard"
            },
            {
                "title": "Automated Data Processing",
                "description": "Masih olah data secara manual? Yuk bikin waktu kerjamu lebih efektif dan efisien pake tools VBA / Macro / Power Query / Python, belum bisa pake tools tersebut? Yaudah sini saya kerjain hehe",
                "imagePrompt": "Automated Data Processing"
            },
            {
                "title": "Buat aplikasi dari Python",
                "description": "Apa itu Python? Python adalah bahasa pemrograman yang multifungsi, dengan Python, kita bisa buat aplikasi yang mempermudah kerjaan kamu, aplikasi ini dapat kamu tentukan apa fungsi dan tujuannya, misal: Aplikasi untuk cek kualitas data, untuk mengubah tipe file dalam satu folder, mengirim email, dsb. semuanya secara otomatis!",
                "imagePrompt": "Python Application"
            }
        ]
    },
    "pageUrl": "/",
    "websiteId": website_id
})
# Adding Contact Section
add_contact_block_response = pyxl_ai__jit_plugin.AddContactsBlock({
    "contacts": {
        "contactsInfos": [
            {"type": "tel", "text": "085155155285"},
            {"type": "name", "text": "Instagram"},
            {"type": "name", "text": "TikTok"}
        ]
    },
    "pageUrl": "/",
    "websiteId": website_id
})
# Adding CTA Button
add_cta_block_response = pyxl_ai__jit_plugin.AddFormBlock({
    "form": {
        "title": "Tertarik? Yuk WA aja yaa 👇",
        "inputs": [
            {"inputName": "Name", "inputType": "text"},
            {"inputName": "Email", "inputType": "email"},
            {"inputName": "Message", "inputType": "textarea"}
        ],
        "sendButtonName": "Send"
    },
    "pageUrl": "/",
    "websiteId": website_id
})
