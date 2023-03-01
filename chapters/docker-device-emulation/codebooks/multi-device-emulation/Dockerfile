FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy device file to container
COPY device1.py .
COPY device2.py .
COPY device3.py .

# Expose port for incoming traffic
EXPOSE 80

# Run devices
CMD ["python", "device1.py"]
CMD ["python", "device2.py"]
CMD ["python", "device3.py"]