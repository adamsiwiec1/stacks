[Bastion Docker](https://hub.docker.com/r/binlab/bastion)


1. Connect to Bastion
Add your user to group docker to have possibility run docker-compose and docker from your user without sudo. After you should re-login or open a new terminal window.
$ sudo usermod -aG docker <your_user>
Create custom work dir e.g. docker, enter to it and clone repository
$ mkdir $HOME/docker 
$ cd $HOME/docker
$ git clone https://github.com/binlab/docker-bastion.git
$ cd docker-bastion
Generate rsa pair (if you have one, skip this)
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f $HOME/.ssh/id_rsa
Add rsa public key to .bastion_keys file
$ cat $HOME/.ssh/id_rsa.pub > $PWD/.bastion_keys
Run docker-compose.yml configuration - bastion & docker-ssh
$ docker-compose up
And then you are can connect to it (in another terminal window)
$ ssh -i $HOME/.ssh/id_rsa -p 22222 bastion@127.0.0.1
You should see like this:
user@localhost:~$ ssh -p 22222 bastion@127.0.0.1
The authenticity of host '[127.0.0.1]:22222 ([127.0.0.1]:22222)' can't be established.
ECDSA key fingerprint is 
SHA256:********************************************
ECDSA key fingerprint is MD5:**:**:**:**:**:**:**:**:**:**:**:**:**:**:**:**.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[127.0.0.1]:22222' (ECDSA) to the list of known hosts.
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <http://wiki.alpinelinux.org>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

bastion:~$ 
2. Connect to Host through Bastion
To achieve this you should add your private key to SSH agent and turn on ForwardAgent in ~/.ssh/config or from a command line via flag -A

-A option enables forwarding of the authentication agent connection.

It means that, it forwards your SSH auth schema to the remote host. > So you can use SSH over there as if you were on your local machine.

Add private key to SSH agent
$ ssh-add $HOME/.ssh/id_rsa
Test Bastion bridge in action
$ ssh -A -J bastion@127.0.0.1:22222 <your_user>@docker-host
3. Connect to another container with SSH through Bastion
$ ssh -A -J bastion@127.0.0.1:22222 bastion@docker-ssh