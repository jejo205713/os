#1. to print values :
echo "hi"
echo "program to print values"

#2.check a value is odd or even :
echo "enter a number :"
read n
if(( $n % 2 == 0 ));then
  echo"$n is even number."
else
  echo"$n is a odd number"
fi

#3.counting (loop):
echo "Counting from 1 to 5:"
for i in {1..5};do
  echo $i
done
