# This is the docker image available. I am using cpu version here. If needed there is gpu version available.
FROM bvlc/caffe:gpu

# Copy the file into docker
COPY requirements.txt requirements.txt

# Run the copied file
RUN pip install -r requirements.txt

# create a folder called model1 and copy all the files in the folder into that folder
ADD . /model1

# Make model1 your work directory
WORKDIR /model1

# Create volumes (folders). one (data) to store data and the other(notebooks) to save your code.
VOLUME ["/model1/data", "/model1/notebooks"]

# Expose your port 8888
EXPOSE 8888

# Run the following command to give a token(password) to your jupyter notebook.
# CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='demo'
