### Process

I thought the easiest way to visualize the buoyancy field was to overlap a body onto the entire field.

However, I couldn't do it because the body would then interact with the floating objects, and move itself away. 

After some trial and error, I came up with another method. I fixed a wall in the buoyancy field, in between the objects and the camera, and lined up the top of the wall with the top of the field. This way, the wall would block off all parts of the objects that are submerged in the field, visualizing the field to an extent. 

In the end, I only added four lines to the original code (line 35-38), and deleted "cube4" (I suppose cube4, which is a line, was used to indicate the top of the buoyancy field, so since now I have "visualized" the field already, I deleted it) 
