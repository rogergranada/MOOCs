#include <string>
#include <fstream>
#include <iostream>


void openCloseFilesExplicitly(){
    // Declare file stream objects (files aren't opened yet).
    //std::ofstream ofile("file1.dat");  // Opens file1.dat for writing.
    //std::ifstream ifile("file1.dat");  // Opens file2.dat for reading.
    //std::fstream  iofile("file1.dat"); // Opens file3.dat for reading/writing.
    //std::fstream iofile3("iofile3.dat", std::ios_base::binary | std::ios_base::in | std::ios_base::out)
    
    //std::ios_base::app // append data to the file
    //std::ios::binary   // read/write binary files

    // Write in a file
    std::ofstream ofile("file1.dat", std::ios_base::app);
    if (ofile.is_open()){
        ofile << "Here is line 1." << std::endl;
        ofile << "Here is line 2." << std::endl;
        ofile << "Here is line 3." << std::endl;
    
        ofile.close();
    }else{
        std::cerr << "Couldn't open file" << std::endl;
    }  

    // Read a file
    std::ifstream ifile("file1.dat");
    if (ifile.is_open()){
        std::string line;
        while (std::getline(ifile, line)){
            std::cout << line << std::endl;
        }

        ifile.close();        
        std::cout << "Finished reading text from file1.txt." << std::endl;
    }
    else{
        std::cerr << "Couldn't open file1.txt for reading." << std::endl;
    }
}

void writeFormattedFile(){
    std::ofstream ofile("peopleFile.txt");
    if (ofile.is_open()){
        ofile << "John" << " " << 42 << " " << 1.67 << std::endl;
        ofile << "Jane" << " " << 41 << " " << 1.54 << std::endl;
        ofile << "Bill" << " " << 35 << " " << 1.82;
        ofile.close();
        
        std::cout << "Finished writing text to peopleFile.txt." << std::endl;
    }
    else{
        std::cerr << "Couldn't open peopleFile.txt for writing." << std::endl;
    }
}

// Read/Write binary file
class tempStat {
    public:
        // Data members.
        double minimum, maximum;

        // Constructor.
        tempStat(double min = 0.0, double max = 0.0) : minimum(min), maximum(max){}

        // Helper method, to write a tempStat object to a file in binary format.
        void write(std::ostream & os){
            os.write((char*)&minimum, sizeof(double));
            os.write((char*)&maximum, sizeof(double));
        }

        // Helper method, to read a tempStat object from a file in binary format.
        void read(std::istream & is){
            is.read((char*)&minimum, sizeof(double));
            is.read((char*)&maximum, sizeof(double));
        }
};

// change operator >>
std::istream& operator >> (std::istream& is, tempStat & ts){
    is >> ts.minimum >> ts.maximum;
    return is;
}
// change operator <<
std::ostream& operator << (std::ostream & os, const tempStat & ts){
    os << ts.minimum << "," << ts.maximum << std::endl;
    return os;
}

// write in the bin file
void writeBinFile(){
    std::ofstream ofile("tempStats.bin", std::ios_base::binary);
    if (ofile.is_open()){
        tempStat(-2.5, 7.5).write(ofile);
        tempStat(0, 9.9).write(ofile);
        tempStat(2.5, 11.0).write(ofile);
        tempStat(5.5, 14.5).write(ofile);
        tempStat(7.0, 17.7).write(ofile);
        tempStat(10.5, 23.7).write(ofile);
        tempStat(11.7, 29.5).write(ofile);
        tempStat(7.6, 22.9).write(ofile);
        tempStat(7.2, 21.5).write(ofile);
        tempStat(2.0, 16.0).write(ofile);
        tempStat(-4.7, 12.5).write(ofile);
        tempStat(-1.9, 8.5).write(ofile);
        ofile.close();
    
        std::cout << "Finished writing binary data to tempStats.bin." << std::endl;
    }
    else{
        std::cerr << "Couldn't open tempStats.bin for writing." << std::endl;
    }
}

void readBinFile(){
    std::ifstream ifile("tempStats.bin", std::ios_base::binary);
    if (ifile.is_open()){
        while (!ifile.eof()){
            tempStat ts;
            ts.read(ifile);
    
            if (ifile.gcount() == 0){
                break;  // If no bytes read, we're done.
            }
            std::cout << "Read temperature stats: " << ts << std::endl;
        }
        ifile.close();
    
        std::cout << "Finished reading binary data from tempStats.bin." << std::endl;
    }
    else{
        std::cerr << "Couldn't open tempStats.bin for reading." << std::endl;
    }
}

int main(){
    //openCloseFilesExplicitly();
    //writeFormattedFile();
    //writeBinFile();
    readBinFile();
    return 0;
}
