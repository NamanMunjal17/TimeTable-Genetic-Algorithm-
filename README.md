# TimeTable Generation using Genetic Algorithm
The code first randomly generates timetables fulfilling needs like:\
* Periods required for each subject in a week
* Availability of teachers for the particular subject
* Block periods
These randomly generated timetables are then put against a fitness checking algorithm. In our the case the fitness score is pretty simple. If the time of two periods clash then we deduct the score achieved by the algo and mutate it with the best performing timetable.\
Mutation method used: Swap\
![Swap method](https://github.com/user-attachments/assets/b5f960a3-061c-426a-b571-b8fb084cf468)\
Credits for image: researchgate.net

# Clean UI
I also built a UI for this project including an admin page, teacher page and a student page. The admin can generate timetable using the algorithm and then can also manually edit it as per their likings. The UI is built with CustomTKinter a library based of TKinter but has a way more clean and modern UI
# Genetic Algorithm Visual representation
![Genetic Algo](https://github.com/user-attachments/assets/246c7723-1967-4226-8cf8-0268a5973003)\
Credits for the image: geekforgeeks
