import sys
import boto
import boto.ec2
import boto.manage.cmdshell

keyname=sys.argv[1]
region=sys.argv[2]

conn_region = boto.ec2.connect_to_region(region)

def delete_key(key_name=keyname):

    ec2 = conn_region 
    ec2.delete_key_pair(key_name)
        

if __name__ == "__main__": 
    delete_key()


