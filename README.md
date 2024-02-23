# commune-datascrapping

This project is to scrap data between all high liquididty pairs (volume over 1 million)
and then predict which pairs will go up or down

1. **Embedding User Content:**
   - Use video2emb, text2emb, and image2emb processes to convert user-generated content into embeddings. These embeddings essentially represent a numerical vector that captures the features of the respective content.

2. **Plotting on a Map:**
   - Assuming the user-generated content has some geographical context, you can plot it on a map using the geographical information associated with the content. This step involves extracting or providing location data linked to the content.

3. **Finding Proximity to Other Points:**
   - Utilize geographical coordinates (latitude and longitude) to calculate the distance between the user-generated content and other points on the map. Various distance metrics such as Euclidean distance or Haversine distance can be used for this purpose.

4. **Scoring Based on Uniqueness:**
   - Develop a scoring mechanism to evaluate the uniqueness of the user-generated content. This might involve analyzing the content itself, considering factors like the diversity of words in text, visual elements in images, or distinctive features in videos. The goal is to quantify how different or unique the content is compared to others.

5. **Integration:**
   - Integrate the above processes into a cohesive system or application that takes user-generated content as input, performs the described steps, and provides output such as the content's location on a map, its proximity to other points, and a uniqueness score.

6. **User Video Embedding:**
   - For videos specifically, consider using a video embedding method that captures temporal and spatial features of the content. This could involve techniques like frame-level embeddings, summarization, or even using pre-trained models for video understanding.

7. **Interactive Visualization:**
   - Provide an interactive visualization to the user, showing the mapped locations of their content and its uniqueness score. This could be a user-friendly interface or dashboard displaying the results.

#To run comscrape
- Go to website/comai
and then run this project

This is a Next.js project created to demonstrate how to run a Next.js application.

Getting Started
To get started with this project, follow the steps below:

Install the dependencies:
1. cd comai
2. npm install
3. Run the development server:
   npm run dev
Open http://localhost:3000 in your browser to see the application running.
