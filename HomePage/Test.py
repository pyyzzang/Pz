
import os
import requests

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    reponse = requests.post('https://www.googleapis.com/youtube/v3/videos',
    params={'token': 'ya29.A0AfH6SMA2Hr5c49y7WT1xUCancj6DrjGnn7xxmsUfCaIt5uhXk7vHAILtR8Y0lzlKFH5G2grP3z8J_4vdYZ2KFZpVldJs6voPTZAxWIkcRA-Znkyfm7MJLZtXsNN0J3f34hQjicH6VJzJt-hhSixCyOMFUlVy'
        ,"chart":"mostPopular"
        ,"part":"snippet"
        ,"regionCode":"kr"
        ,"maxResults":"50"},
    headers = {'content-type': 'application/x-www-form-urlencoded'})
    print(reponse.text)

if __name__ == "__main__":
    main()