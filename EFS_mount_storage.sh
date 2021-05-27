#!/bin/bash 
 
<<COMMENT
rsize=1048576 – Sets the maximum number of bytes of data that the NFS client can receive for each network READ request. This value applies when reading data from a file on an EFS file system. We recommend that you use the largest size possible (up to 1048576) to avoid diminished performance.

wsize=1048576 – Sets the maximum number of bytes of data that the NFS client can send for each network WRITE request. This value applies when writing data to a file on an EFS file system. We recommend that you use the largest size possible (up to 1048576) to avoid diminished performance.

hard – Sets the recovery behavior of the NFS client after an NFS request times out, so that NFS requests are retried indefinitely until the server replies. We recommend that you use the hard mount option (hard) to ensure data integrity. If you use a soft mount, set the timeo parameter to at least 150 deciseconds (15 seconds). Doing so helps minimize the risk of data corruption that is inherent with soft mounts.

timeo=600 – Sets the timeout value that the NFS client uses to wait for a response before it retries an NFS request to 600 deciseconds (60 seconds). If you must change the timeout parameter (timeo), we recommend that you use a value of at least 150, which is equivalent to 15 seconds. Doing so helps avoid diminished performance.

retrans=2 – Sets to 2 the number of times the NFS client retries a request before it attempts further recovery action.

noresvport – Tells the NFS client to use a new Transmission Control Protocol (TCP) source port when a network connection is reestablished. Doing this helps make sure that the EFS file system has uninterrupted availability after a network recovery event.

_netdev – When present in /etc/fstab, prevents the client from attempting to mount the EFS file system until the network has been enabled.
COMMENT
sudo apt-get install nfs-common

sudo mkdir efs

sudo mount - nfs4 -o nfsvers=4.1,rsize=1048576,\
    wsize=1048576,hard,timeo=600,retrans=2,\
    noresvport fs-5006ba07.efs.us-east-1.amazonaws.com:/ efs