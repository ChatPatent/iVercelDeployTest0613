FROM huggingface/transformers-pytorch-cpu:latest

RUN pip install -U pip
RUN pip install torch torchvision datasets transformers

WORKDIR /app

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]