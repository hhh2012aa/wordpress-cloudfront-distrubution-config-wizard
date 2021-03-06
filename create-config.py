import fileinput

s3_replacement_text = input("s3 name: ")
elb_replacement_text = input("elb domain name: ")

s3_replacement_text = s3_replacement_text.replace("\"", "")
elb_replacement_text = elb_replacement_text.replace("\"", "")


# Read in the file
with open('distribution-config.json', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('<s3-name>', s3_replacement_text)
filedata = filedata.replace('<wp-alb-domain>', elb_replacement_text)

# Write the file out again
with open('my-create-CloudFront.json', 'w') as file:
  file.write(filedata)
