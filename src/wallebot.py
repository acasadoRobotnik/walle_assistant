from bottle import run,post,request,response,route
import os
import urllib

@route('/find',method="post")
def gen_path_3():
  postdata = request.forms.get("text")
  output_path = str(urllib.quote(postdata)
  package = {"response_type": "in_channel", "text": "{}".format(output_path)}
  response.content_type = 'application/json'
  return package

if __name__ == '__main__':
  port_config = int(os.getenv('PORT', 5000))
  run(host='0.0.0.0', port=port_config)