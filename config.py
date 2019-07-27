mysql_connection_string = 'mysql://root:root@10.0.0.131/media?charset=utf8'
sa_track_mods = False


# waiting time for phantom js & other functions
DRIVER_WAITING_SECONDS 					= 120
DRIVER_MEDIUM_WAITING_SECONDS 			= 60
DRIVER_SHORT_WAITING_SECONDS 			= 10

# eror status for scraping
ERROR_NONE 								= 0
ERROR_TIMEOUT_EXCEPTION 				= 1
ERROR_RETAILER_PROBLEM 					= 2
ERROR_PROXY_PROVIDER 					= 3
ERROR_403_400 								= 4
ERROR_CAPTCHA_FAILED 					= 5
ERROR_INTERNAL_SERVER 					= 6

ROW_DATA_TYPE_SONG						= "song"
ROW_DATA_TYPE_UNSIGNED_BAND				= "unsigned band"
ROW_DATA_TYPE_SIGNED_BAND				= "signed band"

WEBSITE_SOUND_CLICK						= 0
WEBSITE_SOUND_CLOUD						= 1

proxy_username = "amiel6322"
proxy_password = "proxy11"

proxies = [
	'173.234.169.120:8080',
	'108.62.150.115:8080',
	'108.62.172.34:8080',
	'23.19.153.205:8080',
	'173.234.169.143:8080',
	'108.62.155.198:8080',
	'108.62.195.54:8080',
	'173.208.66.253:8080',
	'173.234.169.149:8080',
	'108.62.195.215:8080',
	'108.62.154.149:8080',
	'108.62.187.218:8080',
	'173.208.12.130:8080',
	'108.62.187.130:8080',
	'108.62.155.108:8080',
	'108.62.154.19:8080',
	'173.208.66.89:8080',
	'108.62.150.11:8080',
	'173.208.12.194:8080',
	'23.19.153.24:8080',
	'23.19.155.177:8080',
	'23.19.155.178:8080',
	'173.234.169.146:8080',
	'173.208.12.11:8080',
	'23.19.154.109:8080',
	'23.19.155.125:8080',
	'108.62.187.95:8080',
	'108.62.150.128:8080',
	'173.208.12.111:8080',
	'108.62.195.178:8080',
	'108.62.150.118:8080',
	'23.19.188.102:8080',
	'108.62.172.144:8080',
	'108.62.172.191:8080',
	'23.19.155.193:8080',
	'108.62.150.13:8080',
	'173.208.48.188:8080',
	'108.62.195.153:8080',
	'108.62.195.167:8080',
	'173.208.12.18:8080',
	'173.208.48.174:8080',
	'108.62.195.49:8080',
	'173.234.169.48:8080',
	'108.62.154.186:8080',
	'173.208.66.34:8080',
	'108.62.151.192:8080',
	'108.62.150.127:8080',
	'23.19.153.115:8080',
	'108.62.154.77:8080',
	'23.19.154.141:8080',
	'173.234.169.37:8080',
	'173.208.12.227:8080',
	'173.234.169.56:8080',
	'108.62.151.91:8080',
	'108.62.195.15:8080',
	'108.62.195.226:8080',
	'23.19.188.123:8080',
	'173.208.48.187:8080',
	'108.62.187.174:8080',
	'23.19.155.102:8080',
	'108.62.187.134:8080',
	'23.19.188.15:8080',
	'108.62.151.247:8080',
	'108.62.172.230:8080',
	'108.62.187.166:8080',
	'108.62.151.234:8080',
	'23.19.153.193:8080',
	'173.234.169.211:8080',
	'173.208.48.181:8080',
	'23.19.155.120:8080',
	'173.234.169.9:8080',
	'108.62.187.136:8080',
	'108.62.151.240:8080',
	'23.19.127.201:8080',
	'108.62.187.89:8080',
	'23.19.153.250:8080',
	'108.62.155.144:8080',
	'173.234.169.202:8080',
	'23.19.127.28:8080',
	'108.62.187.98:8080',
	'23.19.153.2:8080',
	'108.62.154.13:8080',
	'108.62.155.241:8080',
	'108.62.187.133:8080',
	'108.62.195.21:8080',
	'108.62.151.86:8080',
	'108.62.195.162:8080',
	'108.62.155.107:8080',
	'108.62.195.157:8080',
	'23.19.127.96:8080',
	'173.234.169.117:8080',
	'173.208.12.181:8080',
	'23.19.127.44:8080',
	'173.208.12.217:8080',
	'108.62.187.109:8080',
	'173.234.169.227:8080',
	'173.208.12.23:8080',
	'23.19.154.113:8080',
	'23.19.155.153:8080',
	'173.208.66.33:8080',
	'23.19.155.132:8080',
	'23.19.154.133:8080',
	'108.62.155.112:8080',
	'108.62.195.82:8080',
	'108.62.172.116:8080',
	'23.19.188.160:8080',
	'108.62.172.228:8080',
	'173.208.12.155:8080',
	'108.62.154.25:8080',
	'23.19.127.210:8080'
]

info = {
	"soundcloud":
	{
		"root": "https://soundcloud.com"
	},

	"soundclick":
	{
		"root": "https://www.soundclick.com"
	}
}
