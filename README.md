# Lab: Build an MCP Server

This repository contains a backend and infrastructure engineering laboratory project focused on building an **MCP (Model Context Protocol)** Server to expose local datasets, tools, and custom prompt contexts directly to LLM clients.

## 🎯 Project Objective

The goal of this lab is to establish a standardized Model Context Protocol interface. By building an MCP server, the application enables compliant AI models and coding agents (like Claude Desktop or Cursor) to securely connect, programmatically read localized data files, utilize custom search functions, and reason over contextual business data (such as restaurant locations and customer reviews) without manual copy-pasting.

## 📁 Repository Structure

* **`server.py`**: The primary backend engine defining the MCP server lifecycle, handling tool definitions, resource schemas, and streaming protocol requests.
* **`test.py`**: Integration testing script engineered to simulate client payloads, validate server responses, and verify protocol handshake procedures.
* **`California-Culinary-Map.txt`**: Unstructured contextual reference dataset housing regional restaurant data points.
* **`structured-restaurant-data.json` & `augmented-user-review.json`**: Structured relational JSON databases used by the server tools to return accurate context lookups.
* **`.theia/`**: Cloud-based workspace configuration tracking localized editor properties and runtime variables.

## 🛠 Technologies Used

* **Language Core:** Python 3.x
* **Protocol Standard:** Model Context Protocol (MCP SDK)
* **Data Interchange formats:** JSON, Asynchronous I/O (`asyncio`)
* **Network & I/O Communication:** Standard Input/Output streams (stdio) or WebSockets

## 🚀 Installation and Execution

### Local Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Lab-Build-an-MCP-Server
   ```

2. **Install project dependencies:**
   Make sure to install the appropriate MCP Python SDK components:
   ```bash
   pip install mcp requests
   ```

3. **Run the testing script:**
   To verify the server tools are correctly registered and functioning locally, execute the validation script:
   ```bash
   python test.py
   ```

4. **Launch the live MCP server:**
   ```bash
   python server.py
   ```

## 📈 Demonstrated Skills

* **Advanced AI Infrastructure Engineering:** Building standards-compliant developer tooling that directly bridges LLM reasoning capacities with proprietary file systems.
* **Asynchronous Network Interfaces:** Writing clean, thread-safe asynchronous code to handle protocol interactions without processing drops.
* **Context Tool Design:** Packaging nested JSON lookups into standardized semantic actions that LLM clients can dynamically invoke.
