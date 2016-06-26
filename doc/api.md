# LostExhaust API Documentation

The LostExhaust API is split into five different modules: the admin API, the carpool API, the household API, the person API, and the user API.

Note: In this documentation, any placeholder denoted with square brackets (`[...]`) is required. Any placeholder denoted with triangle brackets (`<...>`) is optional and provides a default value. Any use of an ellipsis (`...`) denotes that some content is omitted. GET parameters (following a question mark (`?`) in a URL) are always optional, but if they are not surrounded with triangle brackets, it is recommended and considered good practice to include them.

To use the API, you would make an HTTP request by sending a chosen HTTP verb (GET, PUT, POST, etc,) the parameters necessary to complete the request, and then wait for a response which will be sent in JSON. The URLs to request will take the form:
```
https://[hostname]/api/[api-key]/[module]/[path-to-resource]<?parameter0=value&...>
```
For example, to grab the information about a specific user, you may send a GET request to a URL that looks similar to the following:
```
https://myschool.lostexhaust.org/api/123456789101/user/getinfo/USER1234
```
This will return JSON that enumerates the attributes of a user with the id 'USER1234'. It might look like the following:
```json
{
  "firstname" : "John",
  "lastname" : "Doe",
  "affiliation" : "Student",
  "gradeLevel" : "8",
  "classOf" : "2020",
  "contact" : [
    {
      "type" : "School Email",
      "value" : "john.doe@myschool.edu"
    },
    {
      "type" : "Cell Number",
      "value" : "(000) 000-0000"
    }
  ],
  "households" : [
    "HOUSEHOLD1234"
  ],
  "relationships" : [
    {
      "relationship" : "Mother",
      "user" : "USER1235"
    },
    {
      "relationship" : "Father",
      "user" : "USER1236"
    }
  ]
}
```

### Carpool API

###### Requesting the Nearest Carpools
To receive a list of possible carpools near an address, send a GET request to the following URL with the following parameters:
```
https://[hostname]/api/[api-key]/carpool/findnear/[origin-household-id]?splice_start=[index-to-start]&splice_end=[index-to-end]<&units=[units-for-measurement]>
```
The `[index-to-start]` and the `[index-to-end]` parameters refer to the section of elements in a distance-ordered list of households that should be returned. The distance is measured from `[origin-household-id]` to the household element in units provided with `units`. Valid values for `units` include: `mi` (miles) and `km` (kilometers); the default is `mi`. Every element with an index in the closed set [splice_start, splice_end-1] will be returned. Note: indices are 0-based. For example, if `splice_start=0` and `splice_end=10`, the response will contain information about the 10 nearest households, starting at index 0 (nearest) and ending at index 9 (tenth-nearest). If every parameter is valid and the server encounters no errors, this request will respond with a `200 OK` HTTP response and JSON with the following information:
```json
{
  "carpools" : [
    {
      "index" : [index: int, starting with splice_start],
      "id" : [household-id: string],
      "distance" : [distance from origin-household-id]
    },
    ...
  ]
}
```
If the request fails, the server will respond with either a `400 Bad Request`, a `401 Unauthorized`, a `403 Forbidden`, a `404 Not Found`, or a `500 Internal Server Error`. In the case of any `400` response, the server will respond with JSON that contains the errors:
```json
{
  "errors" : [
    {
      "context" : [context: string|null],
      "reason" : [reason: string],
      "exception" : [exception: string|null]
    },
    ...
  ]
}
```
The context might refer to a variable that has an invalid value, or null if the error occurred for some larger reason, such as if the resource was not found.

### Household API
[To be completed]

###### Requesting Information about a Household
[To be completed]

###### Requesting the Distance to a Household
[To be completed]

### Person API
[To be completed]

###### Requesting Information about a Person
[To be completed]

### User API
[To be completed]

###### Requesting Information about a User
[To be completed]

###### Hiding/Showing User's Household Profile
[To be completed]

###### Hiding/Showing User's Person Profile
[To be completed]

### Admin API
[To be completed]
