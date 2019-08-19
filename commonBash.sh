#/bin/bash
#filename: generate_checksums.sh
PIDARRAY=()
for file in File1.iso File2.iso
do
md5sum $file &
PIDARRAY+=("$!")
done
wait ${PIDARRAY[@]}



(base) vuqt1@hannah:~$ sudo chattr +i immutable
[sudo] password for vuqt1:
(base) vuqt1@hannah:~$ rm immutable
rm: cannot remove 'immutable': Operation not permitted
(base) vuqt1@hannah:~$ sudo rm immutable
rm: cannot remove 'immutable': Operation not permitted

$ rsync -av source_path destination_path
For example,
$ rsync -av /home/slynux/data slynux@192.168.0.6:/home/backups/
data
