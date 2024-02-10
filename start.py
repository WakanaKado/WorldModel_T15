from voyager import Voyager

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
# azure_login = {
#     "client_id": "YOUR_CLIENT_ID",
#     "redirect_url": "https://127.0.0.1/auth-response",
#     "secret_value": "[OPTIONAL] YOUR_SECRET_VALUE",
#     "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
# }
openai_api_key = "ここにAPIキーを入力"

voyager = Voyager(
    openai_api_key= openai_api_key,
    mc_port= 57239,
    # ckpt_dir="save",
    resume = False,
    
)

# start lifelong learning
voyager.learn()