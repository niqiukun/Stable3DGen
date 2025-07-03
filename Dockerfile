# Small base image with Micromamba (~50MB)
FROM mambaorg/micromamba:1.5.5

# Set working dir
WORKDIR /app

# Avoid interactive prompts
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV ENV_NAME=stablex
ENV ENV_PREFIX=/opt/conda/envs/$ENV_NAME

# Copy and create environment
COPY environment.yml .
RUN micromamba create -y -p $ENV_PREFIX -f environment.yml && \
    micromamba run -p $ENV_PREFIX pip install torch==2.4.0 torchvision==0.19.0 \
      --index-url https://download.pytorch.org/whl/cu121 && \
    micromamba clean --all --yes && rm -rf /root/.cache/pip

# Copy app files
COPY . .

# Ensure entrypoint is executable
RUN chmod +x /entrypoint.sh

# Set entrypoint with micromamba env
ENTRYPOINT ["micromamba", "run", "-p", "/opt/conda/envs/stablex", "/entrypoint.sh"]