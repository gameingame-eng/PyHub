using System;
using System.Diagnostics;
using System.Threading;
using System.Management;

class Program
{
    static void Main()
    {
        Console.WriteLine("--- PyHub System Dashboard ---");
        
        try {
            // 1. Get OS Name
            string osName = "Unknown OS";
            ManagementObjectSearcher osSearcher = new ManagementObjectSearcher("SELECT Caption FROM Win32_OperatingSystem");
            foreach (ManagementObject obj in osSearcher.Get()) { osName = obj["Caption"].ToString(); }

            // 2. Get CPU Name
            string cpuName = "Unknown CPU";
            ManagementObjectSearcher cpuSearcher = new ManagementObjectSearcher("SELECT Name FROM Win32_Processor");
            foreach (ManagementObject obj in cpuSearcher.Get()) { cpuName = obj["Name"].ToString(); }

            // 3. Get GPU Name
            string gpuName = "Unknown GPU";
            ManagementObjectSearcher gpuSearcher = new ManagementObjectSearcher("SELECT Name FROM Win32_VideoController");
            foreach (ManagementObject obj in gpuSearcher.Get()) { gpuName = obj["Name"].ToString(); }

            // 4. Get RAM Info
            ManagementObjectSearcher ramSearcher = new ManagementObjectSearcher("SELECT TotalPhysicalMemory FROM Win32_ComputerSystem");
            double totalBytes = 0;
            foreach (ManagementObject obj in ramSearcher.Get()) { totalBytes = Convert.ToDouble(obj["TotalPhysicalMemory"]); }

            PerformanceCounter ramCounter = new PerformanceCounter("Memory", "Available MBytes");
            float freeMB = ramCounter.NextValue();

            double totalGB = totalBytes / 1024.0 / 1024.0 / 1024.0;
            double freeGB = freeMB / 1024.0;

            // Display Results
            Console.WriteLine("OS:         {0}", osName);
            Console.WriteLine("Processor:  {0}", cpuName);
            Console.WriteLine("Graphics:   {0}", gpuName);
            Console.WriteLine("Total RAM:  {0:F2} GB", totalGB);
            Console.WriteLine("Free RAM:   {0:F2} GB", freeGB);
            
            Console.WriteLine("\n--- Live Performance ---");
            PerformanceCounter cpuCounter = new PerformanceCounter("Processor", "% Processor Time", "_Total");
            cpuCounter.NextValue();
            Thread.Sleep(500); // Wait for a real reading
            Console.WriteLine("CPU Load:   {0:F1}%", cpuCounter.NextValue());

        } catch (Exception ex) {
            Console.WriteLine("Error fetching specs: " + ex.Message);
        }

        Console.WriteLine("-----------------------------");
        Console.WriteLine("Press any key to return to PyHub...");
        Console.ReadKey();
    }
}