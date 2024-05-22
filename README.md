<h1 align="left">Project Description 📝</h1>

<p align="left">
The purpose of this project is to create a system capable of detecting the appearance of people and objects in a video provided by the user. Specifically, two detection models were trained: one model capable of detecting two celebrities, Lionel Messi and John Krasinski, and another model capable of detecting two objects: knives or glasses.

For the system to perform the analysis and detection of these objects, users will be able to provide videos or select one of the already available videos previously uploaded to the cloud by other users. Users will be able to choose which celebrity they want to detect, and the objects will be detected by default to simulate the content moderation process. Once the detection process is completed, the system will display a screen with the obtained results, indicating the number of frames in which each of the elements were detected.
</p>

<h2 align="left">Installation instructions 📦</h2>

<p align="left">
Follow these steps to install the project in your local environment:
</p>

<p align="left">
<ol>
  <li>Clone this repository:
    <pre><code>git clone https://github.com/FabSDevX/Proyecto-SO-2.git</code></pre>
  </li>
  <li>Navigate to the API directory:
    <pre><code>cd api</code></pre>
  </li>
  <li>Create your own conda environment:
    <pre><code>conda create --name <my-env></code></pre>
  </li>
  <li>Activate the the conda environment:
    <pre><code>conda activate "your conda environment name"</code></pre>
  </li>
  <li>Install all the dependencies runnning both requirements.txt files in their respective directory (API and objectDetector directories):
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>
</p>

<h2 align="left">Guía de Uso 🚀</h2>

<p align="left">
Once all the installation requirements have been met, follow these steps to use the system:
</p>

<p align="left">
<ol>
  <li>In the front-end directory, run the following command in the terminal:
    <pre><code>npm run dev</code></pre>
  </li>
  <li>In the API directory, you can run it executing the run.py file or running the following command in the terminal:
    <pre><code>python run.py</code></pre>
  </li>
  <li>In the front-end directory, run the following command in the terminal:
    <pre><code>npm run dev</code></pre>
  </li>
</ol>
</p>

<p align="left">
Remember that for the API directory to function, we are using other APIs for the system to work. Therefore, in the API routes file, you need to use your own key for the TMDB API (variable TMDB_API_KEY), your own key for the YT Data API (variable YT_API_KEY), as well as your own connection string for cloud storage with Microsoft Azure Blob Storage (variable CONNECTION_STRING).

Although the system utilizes resources based on your computer's capability, we recommend testing the system first with small-duration and small-sized videos to observe its functionality and your computer's performance, gradually increasing the size of the videos afterward. Keep in mind that the larger the video used, the longer the analysis will take.
</p>

<h2 align="left">Documentación de API 📚</h2>

<p align="left">
La API del sistema ofrece varias funcionalidades para gestionar tareas. A continuación se presentan algunos de los endpoints disponibles:
</p>

<h3 align="left">Obtener todas las tareas</h3>

<p align="left">
<pre><code>GET /api/tareas</code></pre>
Devuelve una lista de todas las tareas.
</p>

<h3 align="left">Crear una nueva tarea</h3>

<p align="left">
<pre><code>POST /api/tareas</code></pre>
Crea una nueva tarea. Ejemplo de cuerpo de la solicitud:
<pre><code>
{
  "titulo": "Nueva Tarea",
  "descripcion": "Descripción de la nueva tarea",
  "fecha_vencimiento": "2024-12-31"
}
</code></pre>
</p>

<h3 align="left">Actualizar una tarea</h3>

<p align="left">
<pre><code>PUT /api/tareas/:id</code></pre>
Actualiza una tarea existente. Ejemplo de cuerpo de la solicitud:
<pre><code>
{
  "titulo": "Tarea Actualizada",
  "descripcion": "Descripción actualizada",
  "fecha_vencimiento": "2024-12-31"
}
</code></pre>
</p>

<h3 align="left">Eliminar una tarea</h3>

<p align="left">
<pre><code>DELETE /api/tareas/:id</code></pre>
Elimina una tarea existente.
</p>

<h2 align="left">Créditos</h2>

<p align="left">
Autor: <a href="https://github.com/tuusuario">Tu Nombre</a>
</p>
