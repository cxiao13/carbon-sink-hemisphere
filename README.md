# # Carbon Sink Hemisphere

## Project Overview

The **Carbon Sink Hemisphere** project aims to identify and analyze the largest carbon sink hemisphere on Earth along with its central pole. This initiative is crucial in understanding and preserving the planet's natural mechanisms for absorbing carbon dioxide, thereby combating climate change.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Illustrations](#illustrations)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The project is designed to determine the hemisphere of the Earth with the highest capacity for carbon sequestration. By pinpointing this crucial location, we gain valuable insights into the Earth's natural processes and can devise better strategies for carbon offsetting and environmental conservation.

## Features

- Identify the largest carbon sink hemisphere.
- Locate the central pole of the identified hemisphere.

## Installation

To get started with the **Carbon Sink Hemisphere** project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/carbon-sink-hemisphere.git
```

2. Navigate to the project directory:

```bash
cd carbon-sink-hemisphere
```

3. Install the required dependencies:

    1. **CDO (Climate Data Operators):**
        - **Linux (Debian-based systems):**
        ```bash
        sudo apt-get update
        sudo apt-get install cdo
        ```

        - **macOS (using Homebrew):**
            ```bash
            brew install cdo
            ```

        - **Windows:**
            - Download the installer from the [CDO website](https://code.mpimet.mpg.de/projects/cdo/files).
            - Follow the installation instructions provided.

        - **Other platforms:**
            - Refer to the [CDO documentation](https://code.mpimet.mpg.de/projects/cdo/embedded/cdo.pdf) for platform-specific instructions.

        Make sure to add the CDO executable to your system's PATH.

    2. **Python Dependencies:**

        For Python dependencies, you can refer to the `requirements.txt` file and provide instructions like:

        ```bash
        pip install -r requirements.txt
        ```
    3. **Slurm Cluster (for parallelization)**:

        Ensure you have access to a Slurm cluster for parallel processing.

## Usage

1. Run the main script for calculation of maximum carbon sink hemisphere:

```bash
python scripts/main.py n # n here should be loop for 0-59, designed specific for slurm job array parallel processing.
chmod +x scripts/merge_grid.sh
./scripts/merge_grid.sh
```

2. Follow the prompts to initiate the analysis.

## Illustrations

For visual aid and better understanding, refer to the [jupyter notebook](./notebooks/carbon_sink_hemisphere.ipynb). This notebook contains diagrams and illustrations that accompany the project.


## Contributing

This project is inspired by Xin Yu, who first came up with the idea.

The original NEE data come from OCN model simulation S3 (Zaehle and Friend (2010), Global Biogeochemical Cycles, GB1005, Zaehle et al. (2011) Nature Geoscience, 4(8), 601-605)

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for more details.

---
