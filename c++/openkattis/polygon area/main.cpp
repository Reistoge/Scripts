#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#define PI 3.14159265
using namespace std;

double product_point(int x1,int y1, int x2, int y2){
    return (x1*x2)+(y1*y2);
}

int main(){
   
    int vertices;
    cin>>vertices;
    
    
    while (vertices!=0){
        bool cw;
        double sum;
        vector<int> polygonX(0);
        vector<int> polygonY(0);
        vector<int> recursive_coordinates(4);
        for(int i=0;i<vertices;i++){

            int x,y=0;
            cin >>x>>y;
            
            if (i < 3){
                polygonX.push_back(x);
                polygonY.push_back(y);

            }
            if(i==2){
                int centerX=polygonX[0];
                int centerY=polygonY[0];
        

                int x1=polygonX[1]-centerX;
                int y1=polygonY[1]-centerY;
                double module1=hypot(x1,y1);
                //cout <<module1<<endl;

                int x2=polygonX[2]-centerX;
                int y2=polygonY[2]-centerY;

                double module2 =hypot(x2,y2);
                //cout <<module2<<endl;
        
        
                double angle=(asin(product_point(x1,y1,x2,y2)/(module1*module2))*180)/PI;
                // cout <<angle<<endl; 
    
                if(angle<0){
                    // cout<<"ccw ";
            
                }
                else if(angle>0){
                    cw=true;
                    // cout<<"cw ";
                }
                if(angle==0){

                    if((x2*y1>0 && x1==0 && y2==0)|| (x1*y2<0 && x2==0 && y1==0)){
                        //cw pp
                        cw=true;
                        //cout<<"cw ";
                    }
                    else if((x1==0 && y2==0 && x2*y1<0)|| (x1*y2>0 && x2==0 && y1==0)){
                        //ccw pp
                        // cout<<"ccw ";

                    }

                }

            }
            
            if(i%2==0){
                
                recursive_coordinates[0]=x;
                recursive_coordinates[1]=y;
            }

            if(i%2!=0){
                 
                recursive_coordinates[2]=x;
                recursive_coordinates[3]=y;

                //for(int i=0; i<4;i++){
                //    cout<<recursive_coordinates[i];
                //}
                
                
                
                

            }
            sum+=(abs(recursive_coordinates[0])*abs(recursive_coordinates[3]))-(abs(recursive_coordinates[1])*abs(recursive_coordinates[2]));
            
            
        }
        //cw or ccw
        if(cw){
            cout<<"cw ";
        }
        else{
            cout<<"CCW ";
        }

       
        cout<<abs(sum/2)<<endl;
        cin >>vertices;
    }

    

    return 0;

}