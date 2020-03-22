# bash/sh

echo "Docker set for dev environment"
sudo apt-get update

read -p "<<<	If above is good to go, Press ENTER to continue. otherwise press ctrl+c	>>>"
echo "sudo apt install apt-transport-https ca-certificates curl software-properties-common"
sudo apt install apt-transport-https ca-certificates curl software-properties-common


read -p "Press ENTER to continue"
echo "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

read -p "Press ENTER to continue"
echo "sudo apt-key fingerprint 0EBFCD88"
sudo apt-key fingerprint 0EBFCD88

read -p "Press ENTER to continue"
echo "sudo add-apt-repository deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

read -p "Press ENTER to continue"
echo "apt-cache policy docker-ce"
apt-cache policy docker-ce

read -p "<<<	If above is good to go, Press ENTER to continue. otherwise press ctrl+c	>>>"
echo "sudo apt-get update"
sudo apt-get update

read -p "<<<	If above is good to go, Press ENTER to continue. otherwise press ctrl+c	>>>"
echo "apt-get install docker-ce docker-ce-cli containerd.io"
sudo apt-get install docker-ce docker-ce-cli containerd.io

read -p "<<<	If above is good to go, Press ENTER to continue. otherwise press ctrl+c	>>>"
echo "docker pull hello-world"
sudo docker pull hello-world

read -p "<<<	If above is good to go, Press ENTER to continue. otherwise press ctrl+c	>>>"
echo "docker run hello-world"
sudo docker run hello-world

read -p "Press ENTER to END"
echo "Docker setup completed"


