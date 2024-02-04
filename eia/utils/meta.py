

def print_metadata(rx):
#---->header  Date  - value:  Sat, 03 Feb 2024 13:47:57 GMT
#---->header  Content-Type  - value:  application/json
#---->header  Transfer-Encoding  - value:  chunked
#---->header  Connection  - value:  keep-alive
#---->header  Vary  - value:  Accept-Encoding
#---->header  Access-Control-Allow-Headers  - value:  Origin, X-Requested-With, Content-Type, Accept, Authorization, X-Params
#---->header  Access-Control-Allow-Methods  - value:  GET,POST
#---->header  Access-Control-Allow-Origin  - value:  *
#---->header  Age  - value:  1
#---->header  Cache-Control  - value:  max-age=0, no-cache, no-store
#---->header  Expires  - value:  Sat, 03 Feb 2024 13:47:57 GMT
#---->header  Pragma  - value:  no-cache
#---->header  Strict-Transport-Security  - value:  max-age=63072000; includeSubdomains;, max-age=31536000; preload
#---->header  Via  - value:  https/1.1 api-umbrella (ApacheTrafficServer [cMsSf ])
#---->header  X-Api-Umbrella-Request-Id  - value:  cddsst51krug5dq9v790
#---->header  X-Cache  - value:  MISS
#---->header  X-Vcap-Request-Id  - value:  50f4a002-8506-4f27-7054-dcd647f5906f
#---->header  X-Frame-Options  - value:  SAMEORIGIN
#---->header  X-Content-Type-Options  - value:  nosniff
#---->header  X-XSS-Protection  - value:  1; mode=block
#---->header  Content-Encoding  - value:  gzip

#a enc:  ascii 
#elapsed:  0:00:00.724514 
# enc:  utf-8 
# permanent_redirect:  False 
#is_redirect:  False 
# links:  {} 
# ok:  False 
#reason:  Not Found 
# status:  404 
# url:  https://api.eia.gov/v2/None?api_key=HCVzjrUOCbriYdp3N9pypOrv8EfQQepgdYVGge3B 

  print('text', rx.text)
  print('status_code', rx.status_code)
