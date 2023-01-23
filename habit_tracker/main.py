import requests

# # pixela_endpoint = "https://pixe.la/v1/users"
parameters = {"token":"kajsjaksaskaskdkasd", 
              "username":"luchy", 
              "agreeTermsOfService":"yes", 
              "notMinor":"yes"
              }

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# graph_endpoint = f"https://pixe.la/v1/users/{parameters['username']}/graphs"
graph_parameters = {"id":"graph-001",
                    "name":"graph-name",
                    "unit":"commit",
                    "type":"int",
                    "color":"shibafu"} 
graph_header = {"X-USER-TOKEN" : parameters["token"]}
# response = requests.post(url=graph_endpoint, headers=graph_header, json=graph_parameters)
# print(response.text)


# https://pixe.la/v1/users/luchy/graphs/graph-001.html

# post a pixel to the graph
# pixel_endpoint = f"https://pixe.la/v1/users/{parameters['username']}/graphs/{graph_parameters['id']}"
pixel_parameters = {"date":"20230119",
                    "quantity":"5",} 
# pixel_response = requests.post(url=pixel_endpoint, headers=graph_header, json=pixel_parameters)
# print(pixel_response.text)


# upd_pixel_endpoint = f"https://pixe.la/v1/users/{parameters['username']}/graphs/{graph_parameters['id']}/{pixel_parameters['date']}"
# upd_pixel_parameters = {"quantity":"16",} 
# upd_pixel_response = requests.put(url=upd_pixel_endpoint, headers=graph_header, json=upd_pixel_parameters)
# print(upd_pixel_response.text)

del_pixel_endpoint = f"https://pixe.la/v1/users/{parameters['username']}/graphs/{graph_parameters['id']}/{pixel_parameters['date']}"
del_pixel_response = requests.delete(url=del_pixel_endpoint, headers=graph_header)
print(del_pixel_response.text)