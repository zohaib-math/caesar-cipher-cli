# Caesar Cipher CLI Tool 🔐

A high-utility, lightweight Command-Line Interface (CLI) application implemented in Python to perform secure text encryption and decryption using the classical Caesar Cipher technique.

---

## 📖 Mathematical Concept

The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down the alphabet. 

Mathematically, the encryption of a character $x$ by a shift $n$ is defined as:

$$E_n(x) = (x + n) \pmod{26}$$

Similarly, decryption is defined as:

$$D_n(x) = (x - n) \pmod{26}$$

---

## ✨ Features

- **Double-Case Support:** Seamlessly encrypts/decrypts both lowercase and uppercase characters while preserving non-alphabetical characters (like punctuation and spaces).
- **Interactive CLI:** Guided user prompts to easily select operations and specify shifting keys.
- **Robust Validation:** Built-in verification mechanisms to ensure shift keys are valid integers within the standard bounds ($1 \leq \text{shift} \leq 25$).

---

## 🛠️ Installation & Usage

### Prerequisites
Make sure you have Python 3 installed on your system.

### Running the Application
Clone the repository and run the script directly from your terminal:

```bash
# Clone this repository
git clone [https://github.com/zohaib-math/caesar-cipher-cli.git](https://github.com/zohaib-math/caesar-cipher-cli.git)

# Navigate to the source directory
cd caesar-cipher-cli/src

# Run the script
python caesar.py
