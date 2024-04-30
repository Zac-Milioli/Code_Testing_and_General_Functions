require 'net/http'
require 'uri'
require 'json'

uri = URI('https://api.chucknorris.io/jokes/random')
response = Net::HTTP.get(uri)
data = JSON.parse(response)['value']

puts data

###############################################################################

uri = URI('https://example.com/api/endpoint')
http = Net::HTTP.new(uri.host, uri.port)
request = Net::HTTP::Post.new(uri.path, {'Content-Type' => 'application/json'})
request.body = {param1: 'valor1', param2: 'valor2'}.to_json

response = http.request(request)
data = JSON.parse(response.body)

puts data

