#include <bits/stdc++.h>
using namespace std;
// optimize the code
// functions for the conditional quicksort.
void swap(vector<int>& arr, int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

 
int partition(vector<int>& arr,vector<int>& arr2, int low, int high)
{
    int pivot = arr[high];
 
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
 
        if (arr[j] < pivot) {
 
            i++;
            swap(arr, i, j);
            swap(arr2,i,j);
        }
    }
    swap(arr, i + 1, high);
    swap(arr2,i+1,high);
    return (i + 1);
}
 
void quickSort(vector<int>& arr,vector<int>& arr2, int low, int high)
{
    if (low < high) {

 
        int pi = partition(arr,arr2, low, high);

 
        quickSort(arr,arr2,low, pi - 1);
        quickSort(arr,arr2, pi + 1, high);
    }
}

 



bool is( int n,vector<int> arr){
    for(int k : arr){
        if(k == n){
            return true;
        }
    }
    return false;
}

int showTeamsBySchool(int k,int c,int school, vector<int> &arr1,vector<int> &arr2,vector<int> &toShow,vector<int> &order){   
    int n=0;
     
    for(int i =0; i<arr1.size();i++){
        if(arr1[i]==0 || arr2[i]==0 ){
            continue;
        }
        else if(arr2[i]==school && n<c && k>0 ) {
             
            toShow.push_back(arr1[i]);
            
            // we save the order of the team to then set the order at the end.
            order.push_back(i);
            
            arr2[i]=0;
            arr1[i]=0;
            
            k--;
            n++;
          
        }

    }
    return n;
}



int main(){

    int n,k,c;
    cin >>n>> k>> c;
    vector<int> teams;
    vector<int> schools;
    vector<int> uniqueSchools;
    vector<int> toShow;
    vector<int> order;
    
    for(int i =0; i<n;i++){
        int team,school;
        cin >> team>> school;
        teams.push_back(team);
        schools.push_back(school);
        if(!is(school, uniqueSchools)){
            uniqueSchools.push_back(school);
        }


    }
    
    while(k>0){
          for(int i=0 ;i<uniqueSchools.size();i++){
                k-=showTeamsBySchool(k,c,uniqueSchools[i],teams,schools,toShow,order);
                if(k==0){
                break;
                }
            }
            
        
    }
    quickSort(order,toShow,0,order.size()-1);
    for(int number : toShow){
        cout<< number<<"\n";
    }

    return 0;

}