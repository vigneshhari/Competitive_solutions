package brainfuckcompiler.code.random;

import brainfuckcompiler.statics;

/**
 *
 * @author vrighter
 */
public class RandomNumberGenerator
{

	int[] temp;
	private int randomh, randoml;

	public RandomNumberGenerator()
	{
		randomh = statics.t.alloc();
		randoml = statics.t.alloc();
		temp = statics.t.alloc(6);
	}

	/**
	 *
	 * @param x
	 */
	public void generateRandomNumber(int x)
	{
		statics.t.clear(temp[0]);
		statics.t.clear(temp[1]);
		statics.t.clear(temp[2]);
		statics.t.clear(temp[3]);
		statics.t.clear(temp[4]);
		statics.t.clear(temp[5]);
		statics.t.move(temp[0], randomh);
		statics.t.move(temp[1], randoml);
		statics.t.plus(temp[3], 7);
		statics.t.loop();
		statics.t.plus(temp[2], 11);
		statics.t.deloop(temp[3]);
		statics.t.loop(temp[2]);
		statics.t.copy(randomh, temp[0], temp[3]);
		statics.t.loop(temp[1]);
		statics.t.inc(randomh);
		statics.t.inc(temp[3]);
		statics.t.inc(temp[4]);
		statics.t.deloop(temp[1]);
		statics.t.move(temp[1], temp[4]);
		statics.t.loop(temp[3]);
		statics.t.inc(randoml);
		statics.t.loop();
		statics.t.inc(temp[4]);
		statics.t.inc(temp[5]);
		statics.t.deloop(randoml);
		statics.t.move(randoml, temp[5]);
		statics.t.inc(temp[5]);
		statics.t.loop(temp[4]);
		statics.t.dec(temp[5]);
		statics.t.celoop(temp[4]);
		statics.t.move(randomh, temp[5]);
		statics.t.deloop(temp[3]);
		statics.t.deloop(temp[2]);
		statics.t.plus(temp[2], 6);
		statics.t.loop(temp[2]);
		statics.t.plus(temp[3], 8);
		statics.t.deloop(temp[2]);
		statics.t.dec(temp[3]);
		statics.t.loop(temp[3]);
		statics.t.copy(randomh,temp[1],temp[2]);
		statics.t.deloop(temp[3]);
		statics.t.clear(temp[0]);
		statics.t.set(temp[1], 5);
		statics.t.loop(temp[1]);
		statics.t.plus(temp[0],5);
		statics.t.deloop(temp[1]);
		statics.t.loop(temp[0]);
		statics.t.inc(randoml);
		statics.t.loop(randoml);
		statics.t.inc(temp[1]);
		statics.t.inc(temp[2]);
		statics.t.deloop(randoml);
		statics.t.move(randoml,temp[2]);
		statics.t.inc(temp[2]);
		statics.t.loop(temp[1]);
		statics.t.dec(temp[2]);
		statics.t.celoop(temp[1]);
		statics.t.move(randomh,temp[2]);
		statics.t.deloop(temp[0]);
		statics.t.plus(temp[0],6);
		statics.t.loop(temp[0]);
		statics.t.plus(randomh,9);
		statics.t.deloop(temp[0]);
		statics.t.copy(x,randomh,temp[0]);
	}

	public void free()
	{
		statics.t.free(temp);
		statics.t.clear(randoml);
		statics.t.clear(randomh);
		statics.t.free(randomh, randoml);
	}
}
