# Curl ia a tool to transfer data to and from a server,
# supporting protocols including HTTP, FTP, IMAP, LDAP, POP3, SCP, SFTP, SMB, SMTP and more

## Web browsing 

###### Fetch HTTP headers 
`curl --head "https://example.com"`

###### List contents of a directory 
`curl --list-only https://example.com/foo/`

###### Redirect query as specified by a 3xx response 
`curl --location https://ians.org`

###### Fail quickly  
`curl --fail-early http://opensource.ga`

###### Check whethe a site is down 
`curl  --head --show-error http://example.com`

###### Expand a shortened  URL 
`curl --head --location https://bit.ly/2yDyS4T`  