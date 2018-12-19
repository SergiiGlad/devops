# !/bin/bash

#
#
# Set group for a number of users as another supplementaru group
#
# note , they will have to re-login
#
#

# add a new group call newgroup

groupadd newgroup

for U in user1 user2 user3 ; do
  usermod --append --groups newgroup $U
done

