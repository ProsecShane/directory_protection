echo "Making preperations..."

# checking if bcrypt is installed
python3 -c "import bcrypt" >/dev/null 2>&1
status=$?

if [ $status -eq 0 ]
then
   echo "'bcrypt' python library already installed."
else
   echo "'bcrypt' python library not installed. Starting installation..."
   
   # try to install bcrypt if not installed
   pip3 install bcrypt >/dev/null 2>&1
   status=$?
   
   if [ $status -eq 0 ]
   then
      echo "'bcrypt' python library successfully installed!"
   else
      # Something went wrong, exiting program
      echo "'bcrypt' python library could not be installed. Exiting."
      exit 1
   fi
fi

echo "Getting files..."

# checking if the files are restricted
cat ./script.py >/dev/null 2>&1
status=$?

echo "Starting program..."
echo ""
if [ $status -eq 0 ]
then
   python3 ./script.py off
else
   # temporarily lifting restrictions
   sudo chattr -i script.py
   sudo chmod 444 script.py
   python3 ./script.py on
fi

echo ""
echo "Program stopped running."
