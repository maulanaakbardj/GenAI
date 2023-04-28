import java.util.Calendar;
import java.util.GregorianCalendar;

public class CalendarGenerator {
    public static void main(String[] args) {
        // Specifies the year for the calendar
        int year = 2023;

        // Create a GregorianCalendar object
        Calendar cal = new GregorianCalendar();

        // Determines the January 1st of the given year
        cal.set(Calendar.YEAR, year);
        cal.set(Calendar.MONTH, Calendar.JANUARY);
        cal.set(Calendar.DAY_OF_MONTH, 1);

        // Display month name and date in calendar format
        String[] months = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
        int month = 0;
        while (cal.get(Calendar.YEAR) == year) {
            month = cal.get(Calendar.MONTH);
            System.out.println("\n" + months[month] + " " + year);
            System.out.println("Su Mo Tu We Th Fr Sa");

            // Specifies the date for each day of the month
            int dayOfWeek = cal.get(Calendar.DAY_OF_WEEK);
            for (int i = 1; i < dayOfWeek; i++) {
                System.out.print("   ");
            }
            for (int i = 1; i <= cal.getActualMaximum(Calendar.DAY_OF_MONTH); i++) {
                System.out.printf("%2d ", i);
                if (((i + dayOfWeek - 1) % 7 == 0) || (i == cal.getActualMaximum(Calendar.DAY_OF_MONTH))) {
                    System.out.println();
                }
            }

            // Determine the next month
            cal.add(Calendar.MONTH, 1);
        }
    }
}
