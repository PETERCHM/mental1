document.addEventListener("DOMContentLoaded", function () {
    var calendarEl = document.getElementById("calendar");
  
    var calendar = new FullCalendar.Calendar(calendarEl, {
      // Options and event data go here
      initialView: "dayGridMonth", // Display month view by default
      events: [
        {
          title: "Mental Health Workshop",
          start: "2023-11-10",
          description: "Join our workshop on mental health.",
        },
        // Add more events as needed
      ],
    });
  
    calendar.render();
  });
  