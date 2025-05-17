# German to French Translation using LLaMA 3.2 Fine-Tuning

This project focuses on fine-tuning Meta's LLaMA 3.2 model using the OPUS Books dataset to perform translation from German to French. The implementation leverages Hugging Face tools and employs the parameter-efficient fine-tuning technique, **QLoRA**. This project was submitted as part of the "Engineering with GenAI" course portfolio (WiSe 2024-25) at RPTU Kaiserslautern.

## 📂 Project Contents

- `genai_portfolio_428443.ipynb` – Jupyter Notebook for data processing, training, evaluation, and UI deployment
- `Portfolio_Report_428443.pdf` – Detailed report covering project design, challenges, evaluation, and reflections
- `README.md` – Overview and instructions

## 🎯 Objective

To fine-tune a general-purpose LLM (LLaMA 3.2-3B) to specialize in translating German sentences into French, comparing performance across different dataset types and analyzing BLEU scores.

## 📊 Datasets Used

### ✅ OPUS Books (Original)
- 1.25M+ multilingual parallel sentences
- Rich linguistic diversity, various sentence lengths and structures

### ✅ Synthetic Dataset
- Generated using `Qwen-2.5-coder-32B-instruct` LLM
- Prompt-based generation with context variety to ensure diversity

### ✅ Combined Dataset
- Union of OPUS and synthetic datasets for broader exposure

### Data Split Ratio
- **70% Training** / **30% Evaluation**
- Dataset A: 1000 pairs → 700 train / 300 test

## 🧠 Model Selection

- **Meta/LLaMA 3.2-3B**: A 3.21B parameter model by Meta AI
- Chosen for size, general-purpose capabilities, and colab compatibility

## 🧪 Fine-Tuning Strategy

- **QLoRA**: Quantized Low-Rank Adaptation
  - 4-bit quantization for memory efficiency
  - Freezes pretrained weights and trains adapter layers
- Chosen to allow fine-tuning in Colab on limited resources

## 📈 Evaluation

- **Metric**: BLEU Score (0 to 100 scale)
  - Measures n-gram overlap with reference translation
- Key findings:
  - **Model C** (synthetic data) achieved best BLEU score
  - Synthetic data outperformed original OPUS dataset
  - Combined data (Model D) did **not** perform best → dataset quality > quantity

## 💡 Key Learnings from Report

- **Synthetic data**, when generated with rich contextual prompts, can **outperform benchmark datasets**
- Model quality is highly sensitive to **prompt design**, **dataset balance**, and **evaluation methods**
- **Interface (Stretch Goal)**: Built using `streamlit`, deployed via `localtunnel` to reduce Colab memory pressure

## 🖥️ Interface

- A lightweight web interface was built to test Model C (best performer)
- Allows real-time translation queries from German to French

## 📌 Setup

### Run Jupyter Notebook
jupyter notebook genai_portfolio_428443.ipynb

### Launch Interface (Required model file)
streamlit run interface_file.py

###🔬 Future Improvements
Compare QLoRA with full fine-tuning on smaller models (e.g., LLaMA 1.3B)

Try other benchmark datasets beyond OPUS Books

Optimize max_new_tokens to avoid irrelevant outputs

Deploy models to the cloud for persistent querying

### ⚖️ Ethical Considerations
Data Usage: OPUS Books is used responsibly for educational purposes

Bias Mitigation: Ensures transparency and evaluates cultural/linguistic bias

Explainability: Translation mistakes are analyzed to identify model limitations

Reproducibility: Synthetic dataset variability may affect reproducibility

### 🙋 Acknowledgements
Meta AI for LLaMA model

Hugging Face for training stack

Qwen team for synthetic dataset generation

RPTU Kaiserslautern – Engineering with GenAI (WiSe 2024-25)

📄 Report Author: Varun Karwa (428443)
🏫 RPTU Kaiserslautern – Department of Computer Science

