def check_status(status):
	#2xx Success
	if status == 200:
		return ("200 OK")
	elif status == 201:
		return ("201 Created")
	elif status == 202:
		return ("202 Accepted")
	elif status == 203:
		return ("203 Non-Authoritative Information")
	elif status == 204:
		return ("204 No Content")
	elif status == 205:
		return ("205 Reset Content")
	elif status == 206:
		return ("206 Partial Content")
	elif status == 207:
		return ("207 Multi-Status")
	elif status == 208:
		return ("208 Already Reported")
	elif status == 226:
		return ("226 IM Used")

	#3xx Redirection
	elif status == 300:
		return ("300 Multiple Choices")
	elif status == 301:
		return ("301 Moved Permanently")
	elif status == 302:
		return ("302 Found")
	elif status == 303:
		return ("303 See Other")
	elif status == 304:
		return ("304 Not Modified")
	elif status == 305:
		return ("305 Use Proxy")
	elif status == 306:
		return ("306 Switch Proxy")
	elif status == 307:
		return ("307 Temporary Redirect")
	elif status == 308:
		return ("308 Permanent Redirect")

	#4xx Client Error
	elif status == 400:
		return ("400 Bad Request")
	elif status == 401:
		return ("401 Unauthorized")
	elif status == 402:
		return ("402 Payment Required")
	elif status == 403:
		return ("403 Forbidden")
	elif status == 404:
		return ("404 Not Found")
	elif status == 405:
		return ("405 Method Not Allowed")
	elif status == 406:
		return ("406 Not Acceptable")
	elif status == 407:
		return ("407 Proxy Authentication Required")
	elif status == 408:
		return ("408 Request Timeout")
	elif status == 409:
		return ("409 Conflict")
	elif status == 410:
		return ("410 Gone")
	elif status == 411:
		return ("411 Length Required")
	elif status == 412:
		return ("412 Precondition Failed")
	elif status == 413:
		return ("413 Payload Too Large")
	elif status == 414:
		return ("414 URI Too Long")
	elif status == 415:
		return ("415 Unsupported Media Type")
	elif status == 416:
		return ("416 Range Not Satisfiable")
	elif status == 417:
		return ("417 Expectation Failed")
	elif status == 418:
		return ("418 I'm a teapot")
	elif status == 421:
		return ("421 Misdirected Request")
	elif status == 422:
		return ("422 Unprocessable Entity")
	elif status == 423:
		return ("423 Locked")
	elif status == 424:
		return ("424 Failed Dependency")
	elif status == 426:
		return ("426 Upgrade Required")
	elif status == 428:
		return ("428 Precondition Required")
	elif status == 429:
		return ("429 Too Many Requests")
	elif status == 431:
		return ("431 Request Header Fields Too Large")
	elif status == 451:
		return ("451 Unavailable For Legal Reasons")

	elif status == 440:
		return ("440 Login Timeout")
	elif status == 449:
		return ("449 Retry With")

	#5xx Server Error
	elif status == 500:
		return ("500 Internal Server Error")
	elif status == 501:
		return ("501 Not Implemented")
	elif status == 502:
		return ("502 Bad Gateway")
	elif status == 503:
		return ("503 Service Unavailable")
	elif status == 504:
		return ("504 Gateway Timeout")
	elif status == 505:
		return ("505 HTTP Version Not Supported")
	elif status == 506:
		return ("506 Variant Also Negotiates")
	elif status == 507:
		return ("507 Insufficient Storage")
	elif status == 508:
		return ("508 Loop Detected")
	elif status == 510:
		return ("510 Not Extended")
	elif status == 511:
		return ("511 Network Authentication Required")

	#Unofficial codes
	elif status == 103:
		return ("103 Checkpoint")
	elif status == 450:
		return ("450 Blocked by Windows Parental Controls")
	elif status == 509:
		return ("509 Bandwidth Limit Exceeded")

	#nginx
	elif status == 444:
		return ("444 No Response (nginx)")
	elif status == 495:
		return ("495 SSL Certificate Error (nginx)")
	elif status == 496:
		return ("496 SSL Certificate Required (nginx)")
	elif status == 497:
		return ("497 HTTP Request Sent to HTTPS Port (nginx)")
	elif status == 499:
		return ("499 Client Closed Request (nginx)")

	#CloudFlare
	elif status == 520:
		return ("520 Unknown Error (CloudFlare)")
	elif status == 521:
		return ("521 Web Server Is Down (CloudFlare)")
	elif status == 522:
		return ("522 Connection Timed Out (CloudFlare)")
	elif status == 523:
		return ("523 Origin Is Unreachable (CloudFlare)")
	elif status == 524:
		return ("524 A Timeout Occurred (CloudFlare)")
	elif status == 525:
		return ("525 SSL Handshake Failed (CloudFlare)")
	elif status == 526:
		return ("526 Invalid SSL Certificate (CloudFlare)")