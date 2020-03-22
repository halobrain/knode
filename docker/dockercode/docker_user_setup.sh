# bash/sh

# Avoid typing sudo whenever you run the docker command

#add your username to the docker group
sudo usermod -aG docker ${USER}

# To apply the new group membership, log out of the server and back in, or type the following:
su - ${USER}
#You will be prompted to enter your user's password to continue.

#Confirm that your user is now added to the docker group by typing:
id -nG

# If you need to add a user to the docker group that you're not logged in as, declare that username explicitly using:
sudo usermod -aG docker username





