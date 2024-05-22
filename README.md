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
  <li>Run the requirement.txt file in the API and ObjectDetector directories
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>
</p>

<h2 align="left">Use guide 🚀</h2>

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
</ol>
</p>

<p align="left">
Remember that for the API directory to function, we are using other APIs for the system to work. Therefore, in the API routes file, you need to use your own key for the TMDB API (variable TMDB_API_KEY), your own key for the YT Data API (variable YT_API_KEY), as well as your own connection string for cloud storage with Microsoft Azure Blob Storage (variable CONNECTION_STRING).

Although the system utilizes resources based on your computer's capability, we recommend testing the system first with small-duration and small-sized videos to observe its functionality and your computer's performance, gradually increasing the size of the videos afterward. Keep in mind that the larger the video used, the longer the analysis will take.
</p>

<h2 align="left">API Documentation 📚</h2>

<p align="left">
A single API was developed as part of the system. Below, It will be described the usage of the developed endpoints and how to make queries to use them:
</p>

<h3 align="left">To check if the API is working</h3>

<p align="left">
<pre><code>GET your_local_host/</code></pre>
This prints a "Hello world" to check if the API is working
</p>

<h3 align="left">To retrieve all available items in the cloud movie storage and the quantity of items</h3>

<p align="left">
<pre><code>GET your_local_host/obtener elementos</code></pre>
This gets you a list of the existing items in the cloud storage and the quantity of items.
</p>

<h3 align="left">To analyze a target video</h3>

<p align="left">
<pre><code>POST your_local_host/procesar_pelicula</code></pre> Performs an analysis of a video already uploaded in cloud storage. Below is an example of the request body:
<pre><code>
{
  "url_pelicula": "https://the/exact/url/of/your/video",
  "name": "leonelMessi"
}
</code></pre>
</p>
Remember that, for the "name" label there are only two famous persons only: leonelMessi and johnKrasinski, so any other name used in that label will cause malfunctioning

<h2 align="left">References for used third-party software 👥</h2>

<p align="left">
Below will be shown all the references used for the development of this project
</p>

<h3 align="left">Repository used as a guide for training our own model</h3>
<p align="left">
Asafbs94 (2022) FaceMask_Glasses_Detector [Source code]. https://github.com/facebookexperimental/Recoil.
https://github.com/Asafbs94/FaceMask_Glasses_Detector
</p>

<h3 align="left">AI used for object detection</h3>
<p align="left">
Ultralytics (2021) yolov5 [Source code]. https://github.com/ultralytics/yolov5
</p>

<h3 align="left">AI used for face detection</h3>
<p align="left">
Adam Geitgey (2017) face-recognition [library]. https://pypi.org/project/face-recognition/
</p>

<h3 align="left">Used Cloud Storage</h3>
<p align="left">
Microsoft (2008) Azure Blob Storage. https://azure.microsoft.com/en-us/products/storage/blobs/
</p>

<h3 align="left">API used to find real movies</h3>
<p align="left">
	TiVo Corporation (2008) TMDB. https://developer.themoviedb.org/reference/intro/getting-started
</p>

<h3 align="left">API used to find real videos</h3>
<p align="left">
	YouTube (2023) YouTubeData API. https://developers.google.com/youtube/v3/docs/videos?hl=es-419
</p>

<h2 align="left">Training process ❗ </h2>
<p align="left">
	To understand more about the training process that was performed to train the yolov5 object detection model, we highly recommend reviewing our process notebook:
</p>

<p align="left">
	https://colab.research.google.com/drive/1uBjiTptZee6XYdsQrHL3ugZGHIUZaYPY?usp=sharing
</p>
